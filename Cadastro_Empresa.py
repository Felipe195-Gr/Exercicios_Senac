from datetime import datetime

nome_completo = input("Digite o nome completo do funcionário: ")
#Pega o início da string até antes da posição do espaço.
espaco = nome_completo.find(" ")
nome = nome_completo[:espaco]

nome_limpo = nome.replace(" ",  "")


#Comeca logo depois do último espaço e vai até o final da string
espaco_2 = nome_completo.find(" ")

sobrenome = nome_completo[espaco_2 + 1:]
nome_limpo2 = sobrenome.replace(" ", "")
nome_limpo3 = nome_limpo + nome_limpo2

ano_nascimento = int(input("Digite o ano de nascimento: "))
aniversario = input("Voce já fez aniversário esse ano(S/N)?").upper()
ano_atual = datetime.now().year

idade = ano_atual - ano_nascimento

if aniversario == "N":
    Idade = (ano_atual - ano_nascimento) - 1
    idade_final = idade - 1
codigo_registro = input("Digite o código de registro (ex: 450_MARKETING_PLENO): ").upper()

nome_completo = nome_completo.title()

email = nome_limpo3 + "." + "@sc.senac.br"


#codigo_registros
#departamento:
underline1 = codigo_registro.find("_", 3)
#level:
underline2 = codigo_registro.rfind("_", 5)
#o que cada underline é:
departamento = codigo_registro [underline1 + 1:]
level = codigo_registro [underline2 + 1:]

if idade < 18:
    print("Você é aprendiz")

if level == "SENIOR":
    print("Diretoria")

else:
    print("Padrão")


print(f"Nome: {nome_completo}")
print(f"Sua idade é: {idade_final}")
print(f"Seu email é:{email}")
print(f"Departamento:{departamento}")
print(f"Nível de acesso:{level}")