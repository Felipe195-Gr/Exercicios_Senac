produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade desejada: "))

cupom_desconto = input("Possui cupom de desconto? (S/N): ").upper()

if cupom_desconto == "S":
    desconto = 0.10

subtotal = preco * quantidade
valor_desconto = subtotal * desconto
total = subtotal - valor_desconto


print("=============== CUPOR FISCAL ===============")
print(f"Produto: {produto}------ R$ {subtotal:.2f}")
print(f"Quantidade: {quantidade}------ R$ {preco:.2f}")
print("---------------------------------------------")
print(f"Desconto: {desconto}------ R$ {valor_desconto:.2f}")
print("---------------------------------------------")
print(f"Valor total: R$ {total:.2f}")