def chamarMenu():
    opcao = int(input("Escolha: \n1 - Registrar ativo \n2 - Persistir em ativo \n3 - Exibir ativos armazenados "))
    return opcao


def registrar(dicionario):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o n° patrimonial: ")] = [input("Digite a data da última atualização: "), input("Digite a descrição: "), input("Digite o  departamento: ")]
        resp = str(input("Deseja continuar? (S/N)").upper())


def persistir(dicionario):
    with open("inventario.csv", "a") as inv:
        for chave, valor in dicionario.items():
            inv.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + valor[2])
    return "Persistindo com sucesso"


def exibir():
    with open("inventario.csv", "r") as inv:
        linhas = inv.readlines()
    return linhas