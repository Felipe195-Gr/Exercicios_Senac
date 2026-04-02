num = float(input("Digite um número (ou 0 para encerrrar): "))
soma = 0

while num != 0:
    soma += num
    num = float(input("Digite um número (ou 0 para encerrar): "))

print("A soma dos números digitados é: ", soma)