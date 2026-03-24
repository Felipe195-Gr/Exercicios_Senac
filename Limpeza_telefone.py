telefone = input("Digite o número de telefone: ")

telefone_limpo1 = telefone.replace(" ", "")
telefone_limpo2 = telefone_limpo1.replace("-", "")
telefone_limpo3 = telefone_limpo2.replace("(","")
telefone_limpo = telefone_limpo3.replace(")","")

print("Número de telefone limpo: ", telefone_limpo)