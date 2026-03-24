nome = input("Digite o nome do funcionário: ")
horas = float(input("Digite o número de horas trabalhadas: "))

if horas > 220:
    extra = horas - 220
    valor_extra = extra * 30 * 0.10

salario = (horas * 30) + valor_extra
fgts = salario * 0.08
inss = salario * 0.11
salario_liquido = salario - fgts - inss

print(f"O salário do funcionário {nome} é: R$ {salario:.2f}")
print(f"O FGTS do funcionário {nome} é: R$ {fgts:.2f}")
print(f"O INSS do funcionário {nome} é: R$ {inss:.2f}")
print(f"O salário líquido do funcionário {nome} é: R$ {salario_liquido:.2f}")