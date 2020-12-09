with open("teste.txt") as arquivo:
    conteudo = arquivo.readlines()

    print("Tipo de dado da variável: ", type(conteudo), "\n")
    print("Conteúdo do arquivo: ", conteudo)