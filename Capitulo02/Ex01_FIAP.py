nome = str(input("Informe seu nome: "))
idade = int(input("Informe sua idade: "))
doenca = str(input("Apresenta suspeita de doença contagiosa? ")).upper()


#PRIMEIRO PROBLEMA A SER RESOLVIDO
if doenca == "SIM":
    print("Paciente {} encaminhado(a) para sala AMARELA.".format(nome.capitalize()))
elif doenca == "NAO":
    print("Paciente {} encaminhado(a) para sala BRANCA.".format(nome.capitalize()))
else:
    print("Informe uma resposta válida (sim/nao)")


#SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65:
    print("Paciente com prioridade.")
else:
    genero = str(input("Informe seu gênero: (F/M)")).upper()
    if genero == "F" and idade > 10:
        gravida= str(input("Paciente está grávida? (SIM/NAO)")).upper()

        if gravida == "SIM":
            print("Paciente com prioridade.")
        else:
            print("Paciente sem prioridade.")
    else:
        print("Paciente sem prioridade.")
