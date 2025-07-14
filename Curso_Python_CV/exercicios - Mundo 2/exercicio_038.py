import termcolor
Valor1 = int(input('\033[1;33mDigite um primeiro valor: '))
Valor2 = int(input('\033[1;34mDigite um segundo valor: '))
print('\033[m')
if Valor1 > Valor2:
    print('\033[1;37mO valor 1 ({}) \033[1;37mé maior que o valor 2 ({})\033[m]'.format(termcolor.colored(Valor1,'green'), termcolor.colored(Valor2, 'red')))
elif Valor2 > Valor1:
    print('\033[1;37mO valor 2 ({}) \033[1;37mé maior que o valor 1 ({})\033[m'.format(termcolor.colored(Valor2,'green'), termcolor.colored(Valor1, 'red')))
else:
    print('Ambos os valores são iguais: valor1 ({}) = valor 2 ({})'.format(termcolor.colored(Valor1,'green'),termcolor.colored(Valor2,'green')))