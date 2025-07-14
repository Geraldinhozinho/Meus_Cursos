import datetime
soma = 0
soma2 = 0
for c in range(1, 8):
    ano_atual = datetime.date.today().year
    ano = int(input('Digite o {}º ano de nascimento: '.format(c)))
    idade = ano_atual - ano
    if idade > 17:
        soma += 1
    else:
        soma2 +=1
if soma < 2:
    print('{} pessoa é de maior'.format(soma))
    print('{} pessoas são de menores'.format(soma2))
elif soma2 < 2:
    print('{} pessoa é de menor'.format(soma2))
    print('{} pessoas são de maiores'.format(soma))
else:
    print('')
    



    