print('\033[1;30;44m======exercício 01 ======\033[m')
print('\033[1;30;45mOlá seja bem-vindo!\033[m')
Nome= input('Qual o seu nome? ')
print('seja bem-vindo \033[1;30;43m',Nome,'\033[m!')
print(' ')


print('======exercício 02 ======')
print('Olá seja bem-vindo!')
Dia= input('Qual o dia de hoje? ')
Mes= input('Qual o mês de hoje? ')
Ano= input('Qual o ano de hoje? ')
print('\033[1;30;42mseja bem-vindo, você nasceu no dia ',Dia,' no mês ',Mes,' e no ano ', Ano,'\033[m')
print(' ')



print('======exercício 03 ======')
print('Olá seja bem-vindo!')
NumeroP= int(input('Qual o primeiro número? '))
NumeroS= int(input('Qual o segundo número? '))
Soma= NumeroP + NumeroS
print('\033[1;30;42mseja bem-vindo\033[1;30;46m {}, a soma entre {} e {} é igual a: {} \033[m'.format(Nome,NumeroP,NumeroS,Soma))
