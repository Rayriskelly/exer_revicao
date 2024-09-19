#Escreva um programa para ler o	ano	de nascimento de uma pessoa e
#escrever uma mensagem que diga	se ela poderá ou não votar este ano
#(não é	necessário considerar o	mês	em que ela nasceu).

ano_nasc = int(input("Digite o ano que você nasceu:"))
ano_atuel = 2024
idade = ano_atuel - ano_nasc

if idade >= 18:
    idade = ano_atuel - ano_nasc
    print(f' Sua idade é {idade} você pode votar esse ano!')

else:
    print(f' Sua idade é {idade} você não pode votar esse ano!')