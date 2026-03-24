print("-------------RegarcasFelipe----------------")
ddd = input("Digite o DDD do telefone: ")
numero = input("Digite o seu numero: ")
operadora = input("Qual é a sua operadora (TIM/VIVO/CLARO): ").upper()
if operadora != "VIVO" and operadora != "TIM" and operadora != "CLARO":
    print("Operadora inválida. Por favor, digite TIM/VIVO/CLARO.")
    exit()

valor_recarga = float(input("Qual é o valor que vc qr colocar: "))
forma_pagamento = input("Qual é a forma de pagamento, 1 (PIX), 2 (CARTÃO) OU 3 (DINHEIRO)")
print("-------------RegarcasFelipe----------------")

taxa = 0

if forma_pagamento == "2":
    taxa = 0.03

subtotal = valor_recarga * taxa
total = valor_recarga + subtotal

print(f"Valor final: R${total:.2f}")

if forma_pagamento == "3":
    valor_recebido = float(input("Qual foi o valor recebido: "))
    troco =  valor_recebido - valor_recarga
    if troco < 0:
        print("Falta dinheiro seu pobre")
    else:
        print(f"o troco é: {troco} 🫵")
        print("-------------RegarcasFelipe----------------")

imprimir_cupom = input("Deseja imprimir o cupom fiscal? (S/N): ").upper()
if imprimir_cupom != "S" and imprimir_cupom != "N":
    print("Resposta inválida. Por favor, digite S ou N.")
    exit()

if imprimir_cupom == "S":
    print("\n--- CUPOM FISCAL ---")
    print(f"Telefone: ({ddd}) {numero}")
    print(f"Operadora: {operadora}")
    print(f"Valor da Recarga: R$ {valor_recarga:.2f}")
    if forma_pagamento == 2:
        print(f"Taxa de Cartão: R$ {taxa:.2f}")
    print(f"Valor Total: R$ {total:.2f}")
    if forma_pagamento == 3:
        print(f"Valor Recebido: R$ {valor_recebido:.2f}")
        print(f"Troco: R$ {troco:.2f}")
    print("--------------------")

    imprimir_cupom = input("Deseja imprimir o cupom fiscal? (S/N): ").upper()
if imprimir_cupom != "S" and imprimir_cupom != "N":
    print("Resposta inválida. Por favor, digite S ou N.")
    exit()

if imprimir_cupom == "S":
    print("\n--- CUPOM FISCAL ---")
    print(f"Telefone: ({ddd}) {numero}")
    print(f"Operadora: {operadora}")
    print(f"Valor da Recarga: R$ {valor_recarga:.2f}")
    if forma_pagamento == 2:
        print(f"Taxa de Cartão: R$ {taxa:.2f}")
    print(f"Valor Total: R$ {total:.2f}")
    if forma_pagamento == 3:
        print(f"Valor Recebido: R$ {valor_recebido:.2f}")
        print(f"Troco: R$ {troco:.2f}")
    print("--------------------")


