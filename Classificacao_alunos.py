alunos_passados = []
alunos_recuperacao = []
alunos_reprovados = []
lista_alunos = []
alunos = int(input("Digite a quantidade de alunos na sala: "))

for aluno in range(alunos):
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a nota do aluno: "))
    nota2 = float(input("Digite a nota do aluno: "))
    media = (nota1 + nota2) /2
    

    if media >=7:
        status = "Aprovado"
        alunos_passados.append(nome)
    elif media >= 5 and media < 7:
        alunos_recuperacao.append(nome)
        status = "Recuperação"
    elif media < 5:
        alunos_reprovados.append(nome)
        status = "Reprovado"

    lista_alunos.append(nome + "-" + str(media) + "-" + status)

for i in lista_alunos:
    nome, media, status = i.split("-")
    print(nome)
    print(media)
    print(status)

print("A quantidade de alunos passados foram:", len(alunos_passados))
print("A quantidade de alunos em recuperação:", len(alunos_recuperacao))
print("A quantidade de alunos reprovados:", len(alunos_reprovados))

soma_medias = 0

for i in lista_alunos:
    nome, media, status = i.split("-")
    soma_medias += float(media)

media_geral = soma_medias / len(lista_alunos)

print("Média geral da turma:", round(media_geral, 2))

maior_media = 0
melhor_aluno = ""

for i in lista_alunos:
    nome, media, status = i.split("-")
    media = float(media)

    if media > maior_media:
        maior_media = media
        melhor_aluno = nome

print("Aluno com a maior média:", melhor_aluno)
print("Maior média:", maior_media)