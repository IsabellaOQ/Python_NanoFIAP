from NanoCourse_FIAP.Capitulo03.Funcoes.IdentificacaoDeFuncoes import *

lista = []

print("\n* PREENCHIMENTO *\n")
preencherInventario(lista)

print("\n* EXIBIÇÃO *\n")
exibirInventario(lista)

print("\n* LOCALIZAR *\n")
localizarPorNome(lista)

print("\n* DEPRECIAR *\n")
depreciarPorNome(lista, 10)

print("\n* EXCLUIR *\n")
excluirPorSerial(lista)

print("\n* EXIBIR NOVO *\n")
exibirInventario(lista)

print("\n* RESUMIR *\n")
resumirValores(lista)