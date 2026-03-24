idade = int(input("Digite a idade da pessoa: "))

if idade < 12 or idade >= 60:
    entrada = "meia entrada"
else:
    entrada = "Entrada inteira"

print("Obrigado por usar nosso sistema de ingresso!")
print("Sua entrada é: ", entrada)

