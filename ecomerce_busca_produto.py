produtos = ["macbook pro", "iphone 17 pro max", "airpods pro", "ipad pro", "apple watch series 6"]
print("------ BUSCA DE PRODUTOS ------")
print("Digite o nome do produto que deseja buscar:")
busca = input("Produto: ").lower() 
if busca in produtos:
    print(f"Produto encontrado: {busca}")
else:
    print(f"Produto não encontrado: {busca}")

    