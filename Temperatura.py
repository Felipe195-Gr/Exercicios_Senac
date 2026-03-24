escala = input("Digite a escala da temperatura (C ou F): ").upper()#função para deixar em maiusculo . lower para deixar em minusculo
temp = float(input("Digitre a temperatura: ").replace(",", ".")) #substitua a vírgula por um ponto

if escala == "C":
    f = (temp * 9/5) + 32
    print(f"{temp:.2f}°C é igual a {f:.2f}°F")

if escala == "f":
    c = (temp - 32) * 5/9
    print(f"{temp:.2f}°F é igual a {c:.2f}°C")

