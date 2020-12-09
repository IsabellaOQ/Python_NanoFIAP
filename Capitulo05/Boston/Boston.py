with open("economic-indicators.csv") as boston:

    total = 0

    ##[1:-1] indica que vai pegar a partir da linha 1 até a última linha -1
    for linha in boston.readlines()[1:-1]:
        total = total + float(linha.split(",")[3])
    print("O total de voos é: ", total)