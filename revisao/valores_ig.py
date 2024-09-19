a = int(input("Digite o valor:"))
b = int(input("Digite o valor:"))

soma = a + b
multiplicar = a * b

c = soma and multiplicar

if a == b:
    c = soma

else:
    c = multiplicar

print(c)

