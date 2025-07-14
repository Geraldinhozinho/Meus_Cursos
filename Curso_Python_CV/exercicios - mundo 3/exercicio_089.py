import time
lista = []
dados = []
media = 0

while True:
    Nome = str(input('\033[1;32mDigite o nome do aluno: '))
    Nota1 = float(input('\033[1;33mDigite a primeira nota do Aluno: '))
    Nota2 = float(input('Digite a segunda nota do Aluno: '))
    print('\033[m')
    media = (Nota1 + Nota2) / 2
    dados.append(Nome)
    dados.append(Nota1)
    dados.append(Nota2)
    dados.append(media)
    lista.append(dados[:])
    dados.clear()
    
    continua = ''
    while continua not in ('S', 'N'):
        continua = str(input('\033[1;36mDeseja continuar[S/N]-> ').strip().upper())[0]
        if continua != 'S' and continua != 'N':
            print('\033[1;31mOps... Tente novamente. \033[m',end='')
    if continua == 'N':
        break
print('\033[m',30*'-=')
print('\033[1;37mNº----- Nome ------------ Média \033[m')
print(20*'-')
for pos, valor in enumerate(lista):
    print(f'{pos}{lista[pos][0]:>12}{lista[pos][3]:>16}')
print(20*'-')
while True:
    resp = ''
    resp = int(input('Deseja mostrar notas de qual aluno: \033[1;33m(999 Interrompe) '))
    if resp == 999:
        print('\033[m')
        break
    if resp >= len(lista):
            print(f'\033[1;31mOps... Tente novamente. Não há essa opção\033[m')
    else:
        print(f'As notas de {lista[resp][0]} são: {lista[resp][1]} , {lista[resp][2]}')
print('FINALIZANDO...')
time.sleep(1)
print(10*'=', 'VOLTE SEMPRE',10*'=')