#lista = []



def preencherInventario(lista):
    resp = "S"
    while resp == "S":
        equip = [
            str(input("Equipamento: ").lower()),
            float(input("Valor: ")),
            int(input("Número Serial: ")),
            str(input("Departamento: "))
        ]
        lista.append(equip)
        resp = str(input("Deseja continuar inserindo? (S/N)").upper())



def exibirInventario(lista):
    for i in lista:
        print("Nome: {}".format(i[0]))
        print("Valor: R${}".format(i[1]))
        print("Serial: {}".format(i[2]))
        print("Departamento: {}".format(i[3]))
        print("\n")



def localizarPorNome(lista):
    busca= str(input("Informe o equipamento que deseja buscar: ").lower())
    for equip in lista:
        if equip[0] == busca:
            print("Nome: ", equip[0])
            print("Valor: R$", equip[1])
            print("Serial: ", equip[2])
            print("Departamento: ", equip[3])



#def depreciarPorNome(lista):
#    depre = str(input("Informe o equipamento a ser depreciado: ").lower())
#    for i in lista:
#        if depre == i[0]:
#            pct = i[1] * 0.10
#            pct = i[1] - pct


#    print("\nEquipamento: {}\nValor anterior: R${}\nDepreciação: R${}".format(i[0], i[1],pct))



def depreciarPorNome(lista, porc):
  depreciacao=input("Digite o nome do equipamento que será depreciado: ")
  for elemento in lista:
    if depreciacao==elemento[0]:
      print("Valor antigo: ", elemento[1])
      elemento[1] = elemento[1] * (1-porc/100)
      print("Novo valor: ", elemento[1])



def excluirPorSerial(lista):
    excluir = int(input("Informe o serial que deseja excluir: "))
    for i in lista:
        if i[2] == excluir:
            lista.remove(i)
            print("\nItens excluídos.")



def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos é de: ", sum(valores))



#print("Funcionou!")