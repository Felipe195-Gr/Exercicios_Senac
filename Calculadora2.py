operacao = input("Digite a operação desejada (+, -, *, /): ")
if operacao not in ['+', '-', '*', '/']:
    print("Operação inválida. Por favor, escolha uma operação válida.")
    exit()

qtd_num = int(input("Digite a quantidade de números que deseja calcular: "))

resultado = 0
for i in range(qtd_num):
    num = float(input(f"Digite o número {i + 1}: "))
    if operacao == '+':
        resultado += num
    elif operacao == '-':
        resultado -= num
    elif operacao == '*':
        if i == 0:
            resultado = num
        resultado *= num
    elif operacao == '/':
        if i == 0:
            resultado = num
        resultado /= num

print(f"O resultado da operação é: {resultado}")