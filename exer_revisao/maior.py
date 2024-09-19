#Escreva um	programa para ler 2	valores	(considere que não serão
#informados	valores	iguais)	e escrever o maior deles.

numero_1 = float(input("Digite o primeiro número:"))
numero_2 = float(input("Digite o segundo número:"))

if numero_1 == numero_2:
    print("Números iguais não são permitidos!")

else:
    if numero_1 > numero_2:
            print(f'{numero_1} é maior que {numero_2}')

    else:
            print(f'{numero_2} é maior que número {numero_1}')