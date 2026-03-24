email = input("Digite o seu email: ")

arroba = email.find("@")
servidor = email[arroba + 1:]

print(f"Servidor: {servidor}")
