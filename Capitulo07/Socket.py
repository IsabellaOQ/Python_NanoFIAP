import socket

resp = "S"

while (resp == "S"):
    url=input("Digite uma url: \nEx: 'www.globo.com'\n")
    ip = socket.gethostbyname(url)
    print("O IP referente a URL informada é: ", ip)
    resp=input("\nDigite 'S' caso queira continuar: ").upper()

print("Obriagada pela atenção!")