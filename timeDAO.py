from classes import *


class TimeDAO:
    def __init__(self, database):
        self.db = database

    def create_time(self, time: Time):  # cria um Teacher
        query = "CREATE (n:Time {nome: $nome,  titulos: $titulos, saldo: $saldo})"
        parameters = {
            "nome": time.nome,
            "titulos": time.titulos,
            "saldo": time.saldo
        }
        self.db.execute_query(query, parameters)

    def get_time(self, nome_time):
        query = "MATCH (n:Time {nome: $nome_time})-[r:JOGOU]-()" \
                "WITH SUM(CASE WHEN r.vencedor = $nome_time THEN 1 ELSE 0 END) AS vitorias," \
                "COUNT(r) AS total_jogos," \
                "n.saldo AS saldo," \
                "SUM(r.gols_$time) as gols_pro " \
                "RETURN " \
                "vitorias * 3 + (total_jogos - vitorias) AS pontos," \
                "total_jogos, vitorias, saldo, gols_pro"

        query = query.replace("$time", nome_time)
        parameters = {
            "nome_time": nome_time
        }
        result = self.db.execute_query(query, parameters)
        return result

    def update_time(self, nome_time, novo_titulos):
        query = "MATCH (t:Time {nome: $nome_time}) SET t.titulos = $novo_titulos"
        parameters = {"nome_time": nome_time, "novo_titulos": novo_titulos}
        self.db.execute_query(query, parameters)

    def delete_time(self, time_nome):
        query = "MATCH (n:Time {nome: $time_nome})" \
                "DETACH DELETE n"
        parameters = {"time_nome": time_nome}
        self.db.execute_query(query, parameters)
