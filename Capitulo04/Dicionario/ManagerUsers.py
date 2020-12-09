
def perguntar():

    opcao = int(input("\nQual opção deseja escolher? \n1 - Inserir \n2 - Pesquisar \n3 - Excluir \n4 - Listar \n5 - Sair\n"))
    return opcao



def inserir(usuarios):

    chave = str(input("informe seu login: ")).upper()
    usuarios[chave] = [
        str(input("Informe seu nome: ")).upper(),
        str(input("Informe sua última data de acesso: ")),
        str(input("Informe sua última estação acessada: ")).upper()
    ]



def busca(usuarios, chave):

    lista = usuarios.get(chave)

    if lista!= None:
        print("Nome: " + lista[0])
        print("Último acesso: " + lista[1])
        print("Última estação: " + lista[2])



def excluir(usuarios, chave):

    if usuarios.get(chave)!= None:
        del usuarios[chave]
        print("Objeto eliminado!")



def listar(usuarios):

    for chave, valor in usuarios.items():
        print('\n')
        print("Login: ", chave)
        print("Dados: ",valor)