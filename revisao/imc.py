peso = float(input("Digite seu peso:"))
altura = float(input("digite sua altura:"))


imc = peso / (altura)**2
print(f'{imc:.2f}')


if imc <= 18.5:
    print("Abaixo do peso")

elif imc >= 18.6 and imc <= 24.9:
    print("Peso ideal (parabéns)")

elif imc >= 25.0 and imc <= 29.9:
    print("Levemente acima do peso")

elif imc >= 30.0 and imc <= 34.9:
    print("Obesidade grau I")

elif imc >= 35.0 and imc <= 39.9:
    print("Obasidade grau II")

elif imc >= 40:
    print("Obesidade grau III (móbida)")



