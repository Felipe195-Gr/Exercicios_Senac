total_itens = int(input("Digite a quantidade do itens:"))
itens_por_caminhao = int(input("Digite a quantidade de itens por caminhão:"))

cargas_completas = total_itens // itens_por_caminhao
sobras = total_itens % itens_por_caminhao

print(f"Serão necessários {cargas_completas} cargas completas.")

if sobras > 0:
    print(f"Restarão {sobras} itens para a última carga.")
