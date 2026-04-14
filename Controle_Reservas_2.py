mesas = {}
while True:
    print("----- CONTROLE DE MESAS -----")
    print(" 1 - Abrir comanda")
    print(" 2 - Consumir itens")
    print(" 3 - Fechar comanda")
    print(" 4 - Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        nome = input("Digite o nome do cliente: ")
        mesa = int(input("Digite o número da mesa: "))
        mesas[mesa] = {"cliente": nome, "itens": []}
        print(f"Comanda aberta para {nome} na mesa {mesa}.")

    elif opcao == 2:
        mesa = int(input("Digite o número da mesa: "))
        if mesa in mesas:
            cardapio = {
                1: {"nome": "Água", "preco": 5.00},
                2: {"nome": "Refrigerante", "preco": 7.00},
                3: {"nome": "Cerveja", "preco": 10.00},
                4: {"nome": "Pizza", "preco": 75.00},
                5: {"nome": "Caipirinha", "preco": 15.00}
            }
            print("---- CARDÁPIO ----")
            for codigo, dados in cardapio.items():
                print(f"{codigo} - {dados['nome']} - R$ {dados['preco']:.2f}")
            
            while True:
                item = int(input("Digite o código do item consumido: [0 para sair] "))
                if item == 0:
                    break
                if item in cardapio:
                    mesas[mesa]["itens"].append(cardapio[item])
                    print(f"{cardapio[item]['nome']} adicionado à comanda da mesa {mesa}.")
                else:
                    print("Item não encontrado no cardápio.")
                

        else:
            print("Mesa não encontrada. Abra uma comanda primeiro.")
    elif opcao == 3:
        mesa = int(input("Digite o número da mesa: "))
        if mesa in mesas:
            total = 0
            print(f"Comanda da mesa {mesa} - Cliente: {mesas[mesa]['cliente']}")
            for item in mesas[mesa]["itens"]:
                print(f"{item['nome']} - R$ {item['preco']:.2f}")
                total += item["preco"]
            print(f"Total a pagar: R$ {total:.2f}")
            del mesas[mesa]
        else:
            print("Mesa não encontrada. Abra uma comanda primeiro.")
    elif opcao == 4:
        print("Encerrando o programa. Até mais!")
        break