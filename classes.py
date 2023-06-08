class Time:
    def __init__(self, nome, titulos):
        self.nome = nome
        self.titulos = titulos
        self.saldo = 0


class Jogo:
    def __init__(self, mandante, visitante, vencedor, gols_mandante, gols_visitante):
        self.mandante = mandante
        self.visitante = visitante
        self.vencedor = vencedor
        self.gols_mandante = gols_mandante
        self.gols_visitante = gols_visitante


class TimeEstatisticas:
    def __init__(self, pontos, total_jogos, vitorias, saldo, gols_pro):
        self.pontos = pontos
        self.total_jogos = total_jogos
        self.vitorias = vitorias
        self.saldo = saldo
        self.gols_pro = gols_pro

    @staticmethod
    def fromResult(result):
        record = result[0]
        pontos = record["pontos"]
        total_jogos = record["total_jogos"]
        vitorias = record["vitorias"]
        saldo = record["saldo"]
        gols_pro = record["gols_pro"]

        time = TimeEstatisticas(pontos, total_jogos, vitorias, saldo, gols_pro)

        return time
