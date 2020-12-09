from NanoCourse_FIAP.Capitulo04.Dicionario.ManagerUsers import *

print("---*---*---"*2)
print("Seja bem-vindo!")
usuarios = {}

opcao = perguntar()

while opcao != 5:
    if opcao == 1:
        inserir(usuarios)
    if opcao == 2:
        busca(usuarios, str(input("Informe a chave que deseja buscar: ")).upper())
    if opcao == 3:
        excluir(usuarios, str(input("Informe qual chave deja excluir: ")).upper())
    if opcao == 4:
        listar(usuarios)
    opcao = perguntar()

print("Programa encerrado!")
