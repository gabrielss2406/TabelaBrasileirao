'''
    Esse arquivo  contem os 3 exercicios, em ordem
    Parte 1 - Questão 1, chamando e exibindo as querys em query.py
    Parte 2 - Questão 2, chamando e exibindo as querys em query.py
    Parte 3 - Questão 3, chamando e exibindo as querys em teacher_crud.py
    Parte 4 - Rodando o TeacherCLI
'''
from database import Database
from classes import *
from timeDAO import TimeDAO
from jogoDAO import JogoDAO

db = Database("bolt://54.160.20.84:7687", "neo4j", "case-rig-blankets")
db.drop_all()

time = Time("Botafogo", 2)
time2 = Time("Cruzeiro", 4)
time3 = Time("Bahia", 2)
time4 = Time("Atletico-MG", 2)

jogo = Jogo("Botafogo", "Cruzeiro", "Botafogo", 2, 1)
jogo2 = Jogo("Botafogo", "Bahia", "Botafogo", 2, 1)
jogo3 = Jogo("Cruzeiro", "Botafogo", "Empate", 2, 2)

q_time = TimeDAO(db)
q_time.create_time(time)
q_time.create_time(time2)
q_time.create_time(time3)
q_time.create_time(time4)
q_time.delete_time("Atletico-MG")
q_time.update_time("Botafogo", 3)

q_jogo = JogoDAO(db)
q_jogo.create_jogo(jogo)
q_jogo.create_jogo(jogo2)
q_jogo.create_jogo(jogo3)

q_jogo.delete_jogo("Botafogo", "Bahia")

q_jogo.update_jogo(Jogo("Botafogo", "Cruzeiro", "Botafogo", 5, 1))

# Retornando stats de time
stats = TimeEstatisticas.fromResult(q_time.get_time("Botafogo"))
print(stats.gols_pro)

# Retornando jogo
s_time1 = "Botafogo"
s_time2 = "Cruzeiro"
game = q_jogo.get_jogo(s_time1, s_time2)
print(game)
print("Gols ", s_time1, ": ", game[f"gols_{s_time1}"])
print("Gols ", s_time2, ": ", game[f"gols_{s_time2}"])
print("Vencedor: ", game["vencedor"])

db.close()
