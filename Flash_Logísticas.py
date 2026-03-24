# Desafio Flash Logística

# Lista para armazenar os produtos
produtos = []

# Coleta de dados dos 10 itens
for i in range(10):
    print(f"\nItem {i+1}:")
    produto = input("Informe o nome do PRODUTO: ")
    valor = float(input("Informe o VALOR (R$): "))
    categoria = input("Informe a CATEGORIA: ")
    dias = int(input("Informe os DIAS para entrega: "))

    # Armazena em um dicionário
    item = {
        "produto": produto,
        "valor": valor,
        "categoria": categoria,
        "dias": dias
    }
    produtos.append(item)

# Tratamento dos dados
faturamento_total = 0
valores = []

print("\n===== RELATÓRIO DETALHADO =====")
for item in produtos:
    valor_final = item["valor"]

    # Aplicar desconto em eletrônicos acima de R$ 4000
    if item["categoria"].lower() == "eletronico" and item["valor"] > 4000:
        valor_final *= 0.95  # desconto de 5%

    # Classificação de urgência
    status_entrega = "URGENTE" if item["dias"] < 10 else "Normal"

    # Atualiza acumuladores
    faturamento_total += valor_final
    valores.append(valor_final)

    # Exibe status do produto
    print(f"Produto: {item['produto']}")
    print(f"Categoria: {item['categoria']}")
    print(f"Valor original: R$ {item['valor']:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")
    print(f"Entrega: {status_entrega}")
    print("-" * 30)

# Cálculo da média
media_valores = faturamento_total / len(produtos)

# Exibe resumo final
print("\n===== RESUMO DO LOTE =====")
print(f"Faturamento total acumulado: R$ {faturamento_total:.2f}")
print(f"Média de valores do lote: R$ {media_valores:.2f}")

