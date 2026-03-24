nome_completo = input("Digite o seu nome completo: ")

espaco = nome_completo.find(" ")

nome = nome_completo[:espaco]

espaco2 = nome_completo.rfind(" ")
sobrenome = nome_completo[espaco2 + 1:]

print(f"Nome: {nome}")
print(F"Sobrenome: {sobrenome}")