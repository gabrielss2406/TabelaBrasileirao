from classes import *


class JogoDAO:
    def __init__(self, database):
        self.db = database

    def create_jogo(self, jogo: Jogo):  # cria um Jogo e atualiza os times
        query = """
                    MATCH (mandante:Time {nome: $time_mandante})
                    MATCH (visitante:Time {nome: $time_visitante})
                    CREATE (mandante)-[j:JOGOU {
                      gols_$mandante: $gols_mandante,
                      gols_$visitante: $gols_visitante,
                      vencedor: $vencedor
                    }]->(visitante)
                    SET mandante.saldo = mandante.saldo + $gols_mandante - $gols_visitante,
                        visitante.saldo = visitante.saldo + $gols_visitante - $gols_mandante
                    """
        query = query.replace("$mandante", jogo.mandante)
        query = query.replace("$visitante", jogo.visitante)

        parameters = {
            "time_mandante": jogo.mandante,
            "time_visitante": jogo.visitante,
            "vencedor": jogo.vencedor,
            "gols_mandante": jogo.gols_mandante,
            "gols_visitante": jogo.gols_visitante
        }

        self.db.execute_query(query, parameters)

    def get_jogo(self, time_mandante, time_visitante):
        query = "MATCH (mandante:Time)-[j:JOGOU]->(visitante:Time) " \
                "WHERE mandante.nome = $time_mandante AND visitante.nome = $time_visitante " \
                "RETURN j"
        parameters = {
            "time_mandante": time_mandante,
            "time_visitante": time_visitante
        }
        result = self.db.execute_query(query, parameters)
        return dict(result[0]["j"])

    def update_jogo(self, jogo: Jogo):
        query = "MATCH (mandante:Time {nome: $time_mandante})-[j:JOGOU]->(visitante:Time {nome: $time_visitante})" \
                "SET mandante.saldo = mandante.saldo - j.gols_$mandante + j.gols_$visitante - $gols_visitante + $gols_mandante," \
                " visitante.saldo = visitante.saldo + j.gols_$mandante - j.gols_$visitante + $gols_visitante - $gols_mandante," \
                "j.gols_$mandante = $gols_mandante, j.gols_$visitante = $gols_visitante, j.vencedor = $vencedor"
        query = query.replace("$mandante", jogo.mandante)
        query = query.replace("$visitante", jogo.visitante)
        parameters = {"time_mandante": jogo.mandante,
                      "time_visitante": jogo.visitante,
                      "gols_mandante": jogo.gols_mandante,
                      "gols_visitante": jogo.gols_visitante,
                      "vencedor": jogo.vencedor}
        self.db.execute_query(query, parameters)

    def delete_jogo(self, time_mandante, time_visitante):
        query = "MATCH (mandante:Time {nome: $time_mandante})-[j:JOGOU]->(visitante:Time {nome: $time_visitante}) " \
                "SET mandante.saldo = mandante.saldo - j.gols_$mandante + j.gols_$visitante, " \
                " visitante.saldo = visitante.saldo - j.gols_$visitante + j.gols_$mandante " \
                "DELETE j "
        query = query.replace("$mandante", time_mandante)
        query = query.replace("$visitante", time_visitante)
        parameters = {"time_mandante": time_mandante, "time_visitante": time_visitante}
        self.db.execute_query(query, parameters)

    def get_tabela(self):
        query = """MATCH (n:Time)-[r:JOGOU]-()
                WITH n.nome AS nome_time,
                     SUM(CASE WHEN r.vencedor = n.nome THEN 1 ELSE 0 END) AS vitorias,
                     SUM(CASE WHEN r.vencedor = 'Empate' THEN 1 ELSE 0 END) AS empates,
                     COUNT(r) AS total_jogos,
                     n.saldo AS saldo,
                     SUM(r["gols_" + n.nome]) AS gols_pro
                RETURN vitorias * 3 + empates AS pontos,
                       total_jogos,
                       vitorias,
                       saldo,
                       gols_pro,
                       nome_time
                ORDER BY pontos DESC, vitorias DESC, saldo DESC, gols_pro DESC, nome_time DESC"""

        result = self.db.execute_query(query)
        return result
