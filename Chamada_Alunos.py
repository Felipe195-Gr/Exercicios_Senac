lista_presentes = []
lista_ausentes = []

for aluno in range(8):
    presente = input(f"O aluno {aluno + 1} está presente? (s/n) ").lower()
    if presente == 's':
        lista_presentes.append(aluno + 1)
    else:
        lista_ausentes.append(aluno + 1)

print("Chamada encerrada!")

listar = input("Deseja listar os alunos presentes? (s/n) ").lower()
if listar == 's':
    print("Alunos presentes:", lista_presentes, "😊")
else: 
    lista_presentes == "0"
    print("Não tem ninguém na sala, pode mexer no celular")

listar_ausentes = input("Deseja listar os alunos ausentes? (s/n) ").lower()
if listar_ausentes == 's':
    print("Alunos ausentes:", lista_ausentes)
else:
    lista_ausentes == "0"
    print("Todos os alunos estão na sala")

print("Tenha um bom dia Professor(a)😊")