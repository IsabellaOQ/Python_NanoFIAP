from NanoCourse_FIAP.Capitulo05.Exercicio_Ativos.Funcoes_ativo import *
dicionario = {}

opcao = chamarMenu()

while 0 < opcao < 4:
    if opcao == 1:
        registrar(dicionario)
    elif opcao == 2:
        persistir(dicionario)
    elif opcao == 3:
        resultado = exibir()

        for linha in resultado:
            lista = linha.split(";")
            print("Data:........ ", lista[1])
            print("Descrição:........", lista[2])
            print("Departamento:.........", lista[3])

    opcao = chamarMenu()