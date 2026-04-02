# Programa para calcular médias e situação dos alunos

alunos = int(input("Digite a quantidade de alunos: "))

aprovados = 0
recuperacao = 0
reprovados = 0
soma_medias = 0
maior_media = 0
aluno_maior_media = ""

for i in range(alunos):
    nome = input(f"\nDigite o nome do aluno {i+1}: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2

    # Determina status
    if media >= 7:
        status = "Aprovado"
        aprovados += 1
    elif media >= 5:
        status = "Recuperação"
        recuperacao += 1
    else:
        status = "Reprovado"
        reprovados += 1

    # Atualiza soma das médias
    soma_medias += media

    # Verifica maior média
    if media > maior_media:
        maior_media = media
        aluno_maior_media = nome

    # Mostra resultado individual
    print(f"\nAluno: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {status}")

# Resumo final
media_geral = soma_medias / alunos
print("\n--- Resumo da Turma ---")
print(f"Total de aprovados: {aprovados}")
print(f"Total em recuperação: {recuperacao}")
print(f"Total de reprovados: {reprovados}")
print(f"Média geral da turma: {media_geral:.2f}")
print(f"Maior média: {maior_media:.2f} (Aluno: {aluno_maior_media})")