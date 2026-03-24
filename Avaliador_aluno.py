nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    situacao = "aprovado"
elif nota >= 5:
    situacao = "recuperação"
else:
    situacao = "reprovado"

print(f"A situação do aluno é: {situacao}")