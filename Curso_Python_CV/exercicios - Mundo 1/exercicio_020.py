import random, termcolor
A1 = input('\033[1;30mInforme o nome do Aluno1: \033[m')
A2 = input('\033[1;31mInforme o nome do aluno2: \033[m')
A3 = input('\033[1;32mInforme o nome do aluno3: \033[m')
A4 = input('\033[1;33mInforme o nome do aluno4: \033[m')

lista = [A1, A2, A3, A4]
random.shuffle(lista)
print(termcolor.colored(lista,'light_red'))