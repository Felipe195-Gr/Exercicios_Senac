cargas = ["REMEDIO-97987-35", "COMIDA-089080-67", "ROUPA-09876-4", "ELETRONICO-09876-54"]
print("-------- LISTA DE CARGAS ----------")
print(" 0 - ", cargas[0])
print(" 1 - ", cargas[1])
print(" 2 - ", cargas[2])
print(" 3 - ", cargas[3])
opcao = int(input("Digite o número da carga que deseja verificar (0-3): "))
if opcao > 3:
    print("Opção inválida")
    exit()
carga = cargas[opcao]

hifen1 = carga.find("-")
categoria = carga[:hifen1]

hifen2 = carga.rfind("-")
dias = carga[hifen2 + 1:]

id = carga[hifen1 + 1:hifen2]

if categoria == "REMEDIO":
    if dias < "10":
        prioridade = 2
    else:
        prioridade = 3

if categoria == "COMIDA":
    if dias > "10" and dias < "30":
        prioridade = 1
    elif dias < "10":
        prioridade = 2
    if dias > "30":
        prioridade = 3

if categoria == "ROUPA":
    if dias < "5":
        prioridade = 1
    else:
        prioridade = 3

if categoria == "ELETRONICO":
    if dias < "5":
        prioridade = 1
    else:
        prioridade = 3