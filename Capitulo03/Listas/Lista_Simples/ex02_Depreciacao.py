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

# DEPRECIAÇÃO
equipDepre = str(input("Informe o nome do equipamento que deseja depreciar: ")).lower()
for buscaEq in range(0, len(equip)):
    if equip[buscaEq] == equipDepre:
        depre = val[buscaEq] * 0.10
        depre = val[buscaEq] - depre
        val = val[buscaEq]

print("\nValor s/ desconto: R${}\nValor c/ depreciação: R${} ".format(val,depre))
