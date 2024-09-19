#a = 5
#b = 6
#c = 4

a = float(input("digite o primeiro número:"))
b = float(input("digite o segundo número:"))
c = float(input("digite o terceiro número:"))

#print("A = 5\nB = 6\nC = 4 ")

soma = a + b
print()
print(f'O resultado da soma é {soma}')
print()

if soma == c:
    print("Os números são iguais")

elif soma > c:
    print("O valor da soma é maior que C")

else:
    print("O valor de C é maior que a soma")