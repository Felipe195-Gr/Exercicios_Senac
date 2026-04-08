sair = 0
pedidos = []
while sair == 0:
    print("------ SISTEMA DE PEDIDO -------")
    print("1 - Fazer um pedido")
    print("2 - Fazer entrega")
    print("3 - Relatório Status do Pedido")
    print("4 - Relatório Geral")
    print("5 - Sair")
    print("--------------------------------")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        nome = input("Digite o nome do cliente: ")
        valor = float(input("Digite o valor do pedido: "))
        local = input("Digite o local de entrega: ")
        status = "Na cozinha"

        if valor <= 0:
            print("Valor do pedido não é aceito.")
        else:
            pedido = str(len(pedidos) + 1) + ";" + nome + ";" + str(valor) + ";" + local + ";" + status
            pedidos.append(pedido)
            print("Pedido registrado com sucesso!")
            print("Número do pedido:", len(pedidos))
            print(pedido)

    elif opcao == 2:
        if len(pedidos) == 0:
            print("Nenhum pedido registrado para entrega.")
        else:
            numero_pedido = int(input("Digite o número do pedido para entrega:"))
            print("Novo status do pedido 1-Saindo para entrega, 2-Entregue")
            status_entrega = int(input("Digite o novo status do pedido: "))
            pedido = pedidos[numero_pedido - 1].split(";")
            if status_entrega == 1:
                pedido[4] = "Saindo para entrega"
            elif status_entrega == 2:
                pedido[4] = "Entregue"
            novo_pedido = pedido[0] + ";" + pedido[1] + ";" + pedido[2] + ";" + pedido[3] + ";" + pedido[4]
            pedidos[numero_pedido - 1] = novo_pedido
    elif opcao == 3:
        pedidos_cozinha = []
        pedidos_saindo = []
        pedidos_entrega = []
        print("Gerando relatório de status do pedido...")
        for p in pedidos:
            pedido = p.split(";")
            if pedido[4] == "Na cozinha":
                pedidos_cozinha.append(pedido)
            elif pedido[4] == "Saindo para entrega":
                pedidos_saindo.append(pedido)
            elif pedido[4] == "Entregue":
                pedidos_entrega.append(pedido)
        
        print("Pedidos na cozinha:")
        print(pedidos_cozinha)
        print("Pedidos saindo para entrega:")
        print(pedidos_saindo)
        print("Pedidos entregues:")
        print(pedidos_entrega)        
            
    elif opcao == 4:
        print("Gerando relatório geral...")
    elif opcao == 5:    
        print("Saindo do sistema...")
        sair = 1

    print("Obrigado por usar o sistema de pedido!")
    print("Sistema encerrado.")