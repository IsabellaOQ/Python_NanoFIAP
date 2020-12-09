equip = []
val = []
numSerial = []
dept = []
cont = 0
resp = "S"




# INSERÇÃO
while resp == "S":
    equip.append(str(input("Equipamento: ").lower()))
    val.append(float(input("Valor: ")))
    numSerial.append(int(input("Número serial: ")))
    dept.append(str(input("Departamento: ")))
    resp = str(input("\nDeseja continuar inserindo? (S/N)\n")).upper()
    cont = cont + 1


# BUSCA
busca = str(input("Deseja buscar algum equipamento? (S/N)")).upper()

if busca == "S":
    busca= str(input("\nInforme o equipamento que deseja buscar: ")).lower()

    for eqBusca in range(0, len(equip)):
        if busca == equip[eqBusca]:
            print("Valor: R${}".format(val[eqBusca]))
            print("Serial: {}".format(numSerial[eqBusca]))
else:
    print("Opção recebida com sucesso!")