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


# EXIBIÇÃO 1
cont1 = 0
print("LISTA: \n")

for i in range(cont):
    print("Equipamento: {}".format(equip[cont1]))
    print("Valor: R${}".format(val[cont1]))
    print("Número serial: {}".format(numSerial[cont1]))
    print("Departamento: {}".format(dept[cont1]))
    print("\n")
    cont1 = cont1 + 1


# ELIMINAÇÃO
buscaDel = int(input("Digite o serial do equipamento que deseja excluir: "))

for delEquip in range(0, len(equip)):
    if numSerial[delEquip] == buscaDel:
        del equip[delEquip]
        del numSerial[delEquip]
        del val[delEquip]
        del dept[delEquip]
        break


# EXIBIÇÃO 2
print("\nLISTA NOVA: \n")

for i in range(0, len(equip)):
    print("Equipamento: {}".format(equip[i]))
    print("Valor: R${}".format(val[i]))
    print("Número serial: {}".format(numSerial[i]))
    print("Departamento: {}".format(dept[i]))
    print("\n")