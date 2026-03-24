mes = int(input("Digite o mês: "))

if mes%2 == 0:
    dias = 30
    if mes == 2:
        dias = 2
else:    
    dias = 31

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