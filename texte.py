nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
escolaridade = input("Digite a sua escolaridade (médio, técnico ou faculdade): ").lower()
experiencia = input("Você tem experiência nessa área (S/N): ").upper()
cidade = input("Você é morador local ou de outra cidade: ").lower()
nota = int(input("Digite a sua nota: "))
trabalhar = input("Aceita trabalhar presencialmente (S/N): ").upper()

# --- Análise principal ---
if idade < 16:
    analise_principal = "Candidato fora da idade mínima"

elif escolaridade == "faculdade":
    if nota >= 8:
        analise_principal = "Candidato com perfil forte"
    else:
        analise_principal = "Candidato com perfil acadêmico em análise"

elif escolaridade == "técnico":
    if experiencia == "S" and nota >= 7:
        analise_principal = "Candidato técnico aprovado na pré-análise"
    else:
        analise_principal = "Candidato técnico em observação"

elif escolaridade == "médio":
    if nota >= 9:
        analise_principal = "Candidato com bom potencial"
    else:
        analise_principal = "Candidato precisa de mais preparação"

else:
    analise_principal = "Escolaridade inválida"

# --- Situação da localização ---
if cidade == "outra" and trabalhar == "N":
    situacao_local = "Não pode seguir para a vaga presencial"
elif cidade == "outra" and trabalhar == "S":
    situacao_local = "Pode participar, mas precisa de deslocamento"
else:
    situacao_local = "Pode participar normalmente"

# --- Resultado de desempenho ---
if nota >= 9 and experiencia == "S":
    desempenho = "Candidato destaque"
elif nota >= 8:
    desempenho = "Bom desempenho na entrevista"
else:
    desempenho = "Desempenho comum na entrevista"

# --- Saída final ---
print("\n--- Resultado Final ---")
print("Senhor(a): ", nome)
print(f"Análise principal: {analise_principal}")
print(f"Situação da localização: {situacao_local}")
print(f"Resultado de desempenho: {desempenho}")