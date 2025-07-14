jogador = {}
lista = []
gols = 0
nome = str(input('Digite o nome do jogador: '))
jogador['Nome'] = nome
partidas = int(input(f'Digite o número de partidas que o {jogador["Nome"]} jogou: '))
for cont in range(1, partidas+1):
    gol = int(input(f'Quantos gols {jogador["Nome"]} fez na {cont}º partida: '))
    gols = gols + gol
    lista.append(gol)
jogador['Gols'] = lista
jogador['Total'] = gols
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {nome} jogou {partidas} partidas.')
for part in range(1, partidas+1):
    print(f'Na partida {part}, fez {jogador["Gols"][part-1]}',end=' ')
    if jogador["Gols"][part-1] == 1:
        print('gol')
    else:
        print('gols')
print('-='*30)
