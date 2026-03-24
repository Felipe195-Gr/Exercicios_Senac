# vendas.py
# Analista de dados - DataMaster BI

# Metas e comissões
def calcular_comissao(venda):
    if venda <= 1000:
        return venda * 0.10
    elif venda <= 5000:
        return venda * 0.15
    elif venda <= 10000:
        return venda * 0.20
    else:
        return venda * 0.25

# Exemplo de vendas por dia (poderia vir de um banco de dados ou input do usuário)
vendas_por_dia = {
    1: 800,
    2: 1200,
    3: 6000,
    4: 9500,
    5: 15000
}

total_vendas = 0
total_comissao = 0
maior_venda = 0
dia_maior_venda = None

for dia, valor in vendas_por_dia.items():
    comissao = calcular_comissao(valor)
    lucro = valor - comissao
    print(f"Dia {dia}: Vendas = R${valor:.2f}, Comissão = R${comissao:.2f}, Lucro = R${lucro:.2f}")

    total_vendas += valor
    total_comissao += comissao

    if valor > maior_venda:
        maior_venda = valor
        dia_maior_venda = dia

print("\nResumo do mês:")
print(f"Total de vendas: R${total_vendas:.2f}")
print(f"Total de comissões: R${total_comissao:.2f}")
print(f"Lucro total: R${total_vendas - total_comissao:.2f}")
print(f"Maior venda: Dia {dia_maior_venda} com R${maior_venda:.2f}")