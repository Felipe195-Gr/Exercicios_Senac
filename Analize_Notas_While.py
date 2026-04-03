nomes = []
notas = []

sair = 0

while sair == 0:
    print("                ")
    print("---Menu---")
    print("1 - Informar a nota")
    print("2 - Relatório de nota")
    print("3 - Sair")
    print("----------")
    print("                ")

    opcao = int(input("Digite a opção desejada: "))
    
    if opcao not in [1, 2, 3]:
        print("Opção inválida. Tente novamente.")
    elif opcao == 3:
        print("Saindo do programa")
        sair = 1

       
    elif opcao == 1:
        nome = input("Informe o nome do aluno: ")
        nomes.append(nome)
        nota = float(input("Informe a nota do aluno: "))
        notas.append(nota)
        
    elif opcao == 2:
        for i in range(len(nomes)):
            print("Aluno:", nomes[i], "| Nota:", notas[i])


