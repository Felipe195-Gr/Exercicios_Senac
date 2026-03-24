#EXTRAIR DADOS DE PRODUTOS

produto1 = "NIKE_CALCADO_2024_798987798"
produto2 = "ADIDAS_VESTUARIO_2025_78992252"
produto3 = "PUMA_ACESSORIOS_2023_789987654"

print("--- LISTA DE PRODUTOS ---")
print("1 - ", produto1)
print("2 - ", produto2)
print("3 - ", produto3)

produto = input("Digite o numero do produto: ")

if produto == '1':
    produto = produto1

if produto == '2':
    produto = produto2

if produto == '3':
    produto = produto3

#NIKE_CALCADO_2024_798987798

underline1 = produto.find("_")
underline2 = produto.find("_", underline1 + 1)
underline3 = produto.find("_", underline2 + 1)

categoria = produto[underline1 + 1:underline2]
ano = produto[underline2 + 1:underline3]

print("Produto escolhido: ", produto)
print("Categoria: ", categoria)
print("Ano: ", ano)