mes = int(input("Digite o mês: "))

if mes%2 == 0:
    dias = 30
    if mes == 2:
        dias = 2
else:    
    dias = 31

total = 0
total_comissao = 0
total_com_comissao = 0
maior_venda = 0
for vendas in range(dias):
    valor = float(input("Digite o valor da venda: "))
    if valor <= 1000:
        comissao = valor * 0.10
    elif valor <= 5000:
        comissao = valor * 0.15
    elif valor <= 10000:
        comissao = valor * 0.20
    else:
        comissao = valor * 0.25
    total += valor
    total_comissao += comissao
    total_com_comissao = total + total_comissao

    if valor > maior_venda:
        maior_venda = valor
        dia_venda = vendas + 1
    
print(f"Total de vendas: R${total:.2f}")
print(f"Total de comissão: R${total_comissao:.2f}")
print(f"Lucro: R${total-total_comissao:.2f}")
print(f"Maior venda: R${maior_venda:.2f} no dia {dia_venda}")