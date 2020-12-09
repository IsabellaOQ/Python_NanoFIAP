ips = {}
resp = "S"

while resp == "S":
    chave1 = input("Digite os dois primeiros octetos: ")
    chave2 = input("Digite os dois últimos octetos: ")

    ips[chave1, chave2] = [input("Nome da máquina: ")]
    resp = input("\nDigite 'S' para continuar: ").upper()


#EXIBIÇÃO DE IP'S
print("\nExibindo ip's:\n")
for ip in ips.keys():
    print(ip[0] + "." + ip[1])


#EXIBIÇÃO DE MÁQUINAS NO MESMO ENDEREÇO
print("\nExibindo máquinas com o mesmo endereço: \n")
pesquisa = input("Digite os dois ultimos octetos: ")

for ip,nome in ips.items():
    if (ip[1] == pesquisa):
        print("\nMáquinas no mesmo enderço (redes diferentes)")
        print(nome)


#EXIBIÇÃO DE MÁQUINAS NA MESMA REDE
print("\nExibindo máquinas que compõem uma mesma rede: \n")
rede = input("Digite os dois primeiros octetos: ")

for ip,nome in ips.items():
    if rede == ip[0]:
        print("\nMáquinas na mesma rede\n")
        print(nome)

#PAREI NA PAGINA 6 A PARTIR DO 'EMAIL'