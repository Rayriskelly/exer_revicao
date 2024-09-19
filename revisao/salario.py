salario_min = 1.293,20
q_salarios = 0

print()
salario_min = float(input("Digite o valor do salário mínimo:"))
salario_use = float(input("Digiite seu salário:"))

q_salarios = salario_use / salario_min

print(f'{q_salarios:.2f}')