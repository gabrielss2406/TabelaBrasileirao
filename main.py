from database import Database
from classes import *
from timeDAO import TimeDAO
from jogoDAO import JogoDAO

db = Database("bolt://54.160.20.84:7687", "neo4j", "case-rig-blankets")
db.drop_all()

q_time = TimeDAO(db)
q_jogo = JogoDAO(db)

#CLI
op = 0
while op != 9:
    op = int(input(f"""-----------Bem Vindo-----------

    [1] - Criar time
    [2] - Atualizar time
    [3] - Deletar tim
    [4] - Stats de um time
    [5] - Adicionar um resultado
    [6] - Atualizar um resultado
    [7] - Deletar um resultado
    [8] - Procurar um resultado
    [9] - Sair

    Sua opção: """))

    if op == 1:
        print("\nCriando Time")
        nome = input("Nome: ")
        titulos = int(input("Titulos: "))
        time = Time(nome, titulos)
        q_time.create_time(time)
    elif op == 2:
        print("\nAtualizar Time")
        nome = input("Nome: ")
        titulos = int(input("Titulos: "))
        q_time.update_time(nome, titulos)
    elif op == 3:
        print("\nAtualizar Time")
        nome = input("Nome: ")
        q_time.delete_time(nome)
    elif op == 4:
        print("\nTime")
        nome = input("Nome: ")
        time = q_time.get_time(nome)
        print(time)
    elif op == 5:
        print("\nCriando jogo")
        time1 = input("Nome: ")
        time2 = input("Nome: ")
        gols1 = int(input("Gols time 1: "))
        gols2 = int(input("Gols time 2: "))
        if gols1 > gols2:
            vencedor = time1
        elif gols2 > gols1:
            vencedor = time2
        else:
            vencedor = "Empate"
        jogo = Jogo(time1, time2, vencedor, gols1, gols2)
        q_jogo.create_jogo(jogo)
    elif op == 6:
        print("\nAtualizando jogo")
        time1 = input("Nome: ")
        time2 = input("Nome: ")
        gols1 = int(input("Gols time 1: "))
        gols2 = int(input("Gols time 2: "))
        if gols1 > gols2:
            vencedor = time1
        elif gols2 > gols1:
            vencedor = time2
        else:
            vencedor = "Empate"
        jogo = Jogo(time1, time2, vencedor, gols1, gols2)
        q_jogo.update_jogo(jogo)
    elif op == 7:
        print("\nDeletanto jogo")
        time1 = input("Nome: ")
        time2 = input("Nome: ")
        q_jogo.delete_jogo(time1, time2)
    elif op == 8:
        print("\nProcurando jogo")
        time1 = input("Nome: ")
        time2 = input("Nome: ")
        jogo = q_jogo.get_jogo(time1, time2)
        print(jogo)
    elif op != 9:
        print("\nOpção invalida!")

db.close()
