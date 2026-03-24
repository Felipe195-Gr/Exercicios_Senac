temp = float(input("Digite a temperatura e graus celcius: "))

if temp < 35:
    situacao = "Temperatura muito baixa"
elif temp <= 37.4:
    situacao = "Temperatura normal"
elif temp <= 38.4:
    situacao = "Estado de atenção"
else:
    situacao = "Febre alta"

dor_corpo = input("Você está sentido dor no corpo? (S/N): ").lower()

recomendacao = "Nenhuma recomendação adicional"
# a terminar