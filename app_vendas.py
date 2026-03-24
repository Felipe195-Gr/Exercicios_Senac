vendas = [100, 200, 300, 400, 500, 456, 897, 888, 777, 8722, 1234, 5678]
print("------ METRICAS DE VENDAS ------")
print(" 1 - Total de vendas")
print(" 2 - Média de vendas")
print(" 3 - Maior venda")
print(" 4 - Menor venda")
print(" 5 - Meta batida")
print(" 6 - Sair")
print("---------------------------------")
metrica = input("Escolha a métrica que deseja calcular: ")

if metrica == "1":
    total_vendas = sum(vendas)
    print(f"Total de vendas: {total_vendas}")
if metrica == "2":
    media_vendas = sum(vendas) / len(vendas)
    print(f"Média de vendas: {media_vendas}")
if metrica == "3":
    maior_venda = max(vendas)
    print(f"Maior venda: {maior_venda}")
if metrica == "4":
    menor_venda = min(vendas)
    print(f"Menor venda: {menor_venda}")
if metrica == "5":
    meta = 50000
    total_vendas = sum(vendas)
    if total_vendas >= meta:
        print("Meta batida!")
    else:
        print("Meta não batida.")
if metrica == "6":
    print("Saindo do programa...")
    exit()