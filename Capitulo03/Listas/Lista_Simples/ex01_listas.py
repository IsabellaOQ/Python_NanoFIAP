equip = []
val = []
numSerial = []
dept = []
cont = 0
resp = "S"



# INSERÇÃO
while resp == "S":
    equip.append(str(input("Equipamento: ")))
    val.append(float(input("Valor: ")))
    numSerial.append(int(input("Número serial: ")))
    dept.append(str(input("Departamento: ")))
    resp = str(input("\nDeseja continuar inserindo? (S/N)\n")).upper()
    cont = cont + 1



# EXIBIÇÃO DA LISTA
cont1 = 0
print("LISTA: \n")

for i in range(cont):
    print("Equipamento: {}".format(equip[cont1]))
    print("Valor: R${}".format(val[cont1]))
    print("Número serial: {}".format(numSerial[cont1]))
    print("Departamento: {}".format(dept[cont1]))
    print("\n")
    cont1 = cont1 + 1

print("O usuário inseriu {} vezes.\n".format(cont))



# LISTAS SEPARADAS
pergunta = str(input("Deseja exibir alguma lista específica? (S/N)\n")).upper()

while pergunta == "S":
    exLista = int(input("Qual das listas deseja visualizar? \n1- Equipamentos \n2- Valores inseridos \n3- Números seriais \n4- Departamentos\n"))

    #lista 1
    if exLista == 1:
        print("Equipamentos: \n")
        cont1 = 0

        for i in range(cont):
            print(equip[cont1] + "\n")
            cont1 = cont1 + 1
        print("\n")

    #lista 2
    elif exLista == 2:
        print("Valores: \n")
        cont1 = 0
        total = 0
        for i in range(cont):
            print("R$ {}\n".format(val[cont1]))

            total = val[cont1] + total
            cont1 = cont1 + 1
        print("Total: R$ {:.2f}".format(total))
        print("\n")

    #lista 3
    elif exLista == 3:
        print("Números seriais: \n")
        cont1 = 0
        for i in range(cont):
            print("{}° - {}".format(cont1, numSerial[cont1]))
            cont1 =cont1 + 1
        print("\n")

    #lista 4
    elif exLista == 4:
        print("Departamentos: \n")
        cont1 = 0

        for i in range(cont):
            print("- {}".format(dept[cont1]))
            cont1 = cont1 + 1

    else:
        print("Escolha uma exibição válida.")

    pergunta = str(input("Deseja exibir mais alguma lista? (S/N)\n")).upper()

else:
    print("Opção recebida com sucesso.")















