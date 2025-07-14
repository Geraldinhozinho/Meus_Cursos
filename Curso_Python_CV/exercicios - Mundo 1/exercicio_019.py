import random,termcolor
A1 = input(termcolor.colored('Informe o nome do Aluno1: ','magenta','on_green'))
A2 = input('\033[1;32;40mInforme o nome do aluno2: \033[m')
A3 = input('Informe o nome do aluno3: ')
A4 = input('Informe o nome do aluno4: ')

lista = [A1, A2, A3, A4]
escolhido = random.choice(lista)
print('O aluno escolhido é: {}'.format(escolhido))