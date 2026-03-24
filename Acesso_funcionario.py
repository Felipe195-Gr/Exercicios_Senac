cargo = input("Digite o cargo do funcionário: ").lower()
horario = int(input("Digite o horário atual (0-23): "))

cargo = cargo.replace("é", "e")

if cargo == "gerente":
    acesso = "Acesso total liberado"
elif cargo == "supervisor" and horario >= 8 and horario <= 18:
    acesso = "Acesso liberado no horarário comercial"
elif cargo == "tecnico" and horario >= 9 and horario <= 17:
    acesso = "Acesso liberado para manutenção"
else:
    acesso = "Acesso negado"

print(acesso)