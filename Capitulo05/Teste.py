with open("teste.txt", "w") as teste:
    teste.write("Nunca foi tão fácil criar um arquivo!")

with open("teste.txt", "a") as teste:
    teste.write("\nContinuação do texto.")