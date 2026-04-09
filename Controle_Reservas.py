sair = 0
num_mesa_ocupada = []
while sair == 0:
    print("------ SISTEMA DE RESERVAS -------")
    print("1 - Fazer uma reserva")
    print("2 - Remover uma reserva")
    print("3 - Mesas Ocupadas")
    print("4 - Sair")
    print("--------------------------------")

    opcao = int(input("Digite a opção desejada: "))

#Validação da opção escolhida, considerando as opções disponíveis de 1 a 4
    if opcao < 1 or opcao > 4:
        print("Opção inválida. Por favor, escolha uma opção entre 1 e 4.")
        continue
    
    if opcao == 1:
        nome = input("Digite o seu nome: ")
#Validação do número da mesa, considerando o limite de 20 mesas e a verificação de mesas ocupadas
        num_mesa = int(input("Digite o número: "))
        if num_mesa <= 0:
            print("Número da mesa inválido. A reserva não pode ser feita.")
            continue
        elif num_mesa > 20:
            print("A quantidade de mesas é limitada a 20. A reserva não pode ser feita.")
            continue
        elif num_mesa in num_mesa_ocupada:
            print("Mesa ocupada.")
            continue
        else:
            print("Mesa disponível.")
            num_mesa_ocupada.append(num_mesa)
#Validação da quantidade de pessoas, considerando o limite de 10 pessoas por reserva
        quant_pessoas = int(input("Digite o número de pessoas: "))
        if quant_pessoas <= 0:
            print("Quantidade de pessoas inválida. A reserva não pode ser feita.")
            continue
        elif quant_pessoas > 10:
            print("A quantidade de pessoas é limitada a 10. A reserva não pode ser feita.")
            continue
        horario = int(input("Digite o horário: "))

#validação do horário, considerando o horário de funcionamento do restaurante das 18h às 24h
        if horario >= 18 and horario <= 24:
            print("Horário válido.")
        else:            
            print("Horário inválido. A reserva não pode ser feita.")
            continue
#Exibição dos detalhes da reserva, caso todas as validações sejam aprovadas
        print("------ RESERVA -------")
        print("Reserva registrada com sucesso!")
        print("Nome:", nome)
        print("Número da mesa:", num_mesa)
        print("Quantidade de pessoas:", quant_pessoas)
        print("Horário:", horario)
        print("-----------------------")
    
    elif opcao == 2:
        num_mesa = int(input("Digite o número da mesa para remover a reserva: "))
#Validação do número da mesa para remoção, considerando o limite de 20 mesas e a verificação de mesas ocupadas
        if num_mesa in num_mesa_ocupada:
            num_mesa_ocupada.remove(num_mesa)
            print(f"Reserva da mesa {num_mesa} removida com sucesso!")
        else:
            print("Essa mesa não está reservada.")
#Exibição do número de mesas ocupadas e a lista de mesas ocupadas, caso o usuário escolha a opção 3
    if opcao == 3:
        print(len(num_mesa_ocupada), "mesas ocupadas.")
        print("Mesas ocupadas:", num_mesa_ocupada)
#Exibição de mensagem de saída do sistema, caso o usuário escolha a opção 4
    elif opcao == 4:
        print("Saindo do sistema de reservas...")
        sair = 1


# Não deve permitir quantidade inválida nem reservar uma mesa já ocupada. Também deve permitir
# remover uma reserva e listar as mesas disponíveis e reservadas. O programa deve continuar executando até o
# usuário escolher sair.