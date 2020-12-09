usuario= {}

usuario = {
    "Harry" : ["Harry Potter", "19/10/2020", "Ministério da Magia"],
    "Rony" : ["Ronald Weasley", "18/10/2020", "Beco Diagonal"],
    "Mione" : ["Hermione Granger", "17/10/2020", "Floresta Proibida"]
}

usuario ["Hagrid"] = ["Rúbeo Hagrid", "17/10/2020", "Floresta Proibida"]


#Exibição de todos os usuários
print("\nUSUÁRIOS:\n\n{}\n".format(usuario))


print("---*---"*8)

#Exibição de um usuário específico
print("\n{}\n{}".format(usuario.get("Mione"), usuario.get("Hagrid")))
