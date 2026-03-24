lista_produtos = ["Mouse-10", "Teclado-2", "Monitor-5", "Webcam-0"]

for produto in lista_produtos:
    nome, quantidade = produto.split("-")

    # print(f"Produto: {nome}, Quantidade: {quantidade}")
    if int(quantidade) < 5:
        print(f"Produto {nome} com estoque baixo! Quantidade: {quantidade}")