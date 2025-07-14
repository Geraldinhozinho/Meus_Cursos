import termcolor
Salario = float(input('Digite o valor do seu salário: '))

if Salario >= 1250:
    Novo = Salario + (Salario*10/100)
    print('Salário anterior era {}, agora seu salário agora é: {}'.format(termcolor.colored(f'{Salario:.2f}', 'red'),termcolor.colored(f'{Novo:.2f}', 'green')))
else:
    Novo = Salario + (Salario*15/100)
    print('Salário anterior era {}, agora seu salário agora é: {}'.format(termcolor.colored(f'{Salario:.2f}', 'red'),termcolor.colored(f'{Novo:.2f}', 'green')))