print("-----------------------------Trasportadora Felipe -----------------------------")
tipo_produto = input("Digite o tipo do seu produto: ").lower()
peso_carga = float(input("Digite o peso do seu produto: "))
distancia_entrega = input("Digite a distância da entrega do seu produto: ")

tipo_produto = tipo_produto.replace("à", "a")
tipo_produto = tipo_produto.replace("ô", "o")

print("-----------------------------Trasportadora Felipe -----------------------------")

if tipo_produto == "fragil" and peso_carga > 10:
    status = "Transporte especial obrigatório"
elif tipo_produto == "fragil" and peso_carga < 10:
    status = "Transporte cuidadoso"

elif tipo_produto == "alimento" and distancia_entrega > 300:
    status = "Verificar prazo e refrigeração"

elif tipo_produto == "alimento" and distancia_entrega < 300:
    status = "Entrega comum de alimento"

elif tipo_produto == "eletronico" and peso_carga > 20:
    status = "Carga eletrônica pesada"

elif tipo_produto == "eletronico" and peso_carga < 20:
    status = "Carga eletrônica padrão"

elif tipo_produto == "outros produtos" and distancia_entrega > 500:
    status = "Entrega longa"
else: 
    status = "Entrega normal"

print("O status da sua carga é: ",status)
print("-----------------------------Trasportadora Felipe -----------------------------")



