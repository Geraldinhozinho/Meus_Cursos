import time
Jogadores = {}
lista = []
lista_dic = []
while True:
    nome_jogador = str(input('Digite o nome do jogador: '))
    Jogadores['Nome'] = nome_jogador
    partidas_jogador = int(input(f'Digite quantas partidas {Jogadores["Nome"]} jogou: '))
    for cont in range(1, partidas_jogador+1):
        gol = int(input(f'Quantos gols foram feitos na {cont}ª partida: '))
        lista.append(gol)
    Jogadores['Gols'] = lista[:]
    lista_dic.append(Jogadores.copy())
    lista.clear()
    continua = ' '
    while continua not in ('S', 'N'):
        continua = str(input('Deseja continuar? [S, N]: ')).upper().strip()
        
        if continua != 'S' and continua != 'N':
            print('Tente novamente... Apenas [S ou N]')
    if continua == 'N':
        break

# lista_dic = [
#     {'nome': 'Alana', 'gols': [1, 2, 3], 'total': 6},
#     {'nome': 'Geraldo', 'gols': [0, 1], 'total': 1},
#     {'nome': 'Carlos', 'gols': [2, 2, 1, 0], 'total': 5}
# ]


cod = 'Cod Nomes'
cod1 = 'gols'
cod2 = 'total'
print('=-'*30)
print(f'{cod:-^20}{cod1:-^20}{cod2:-^20}')
print('=-'*30)
for k, v in enumerate(lista_dic):
    print(f'{k:>4} {lista_dic[k]["Nome"]:<22} {str(lista_dic[k]["Gols"]):20} {sum(lista_dic[k]["Gols"]):<20}')
print('=-'*30)

while True:
    dados = int(input('Deseja mostrar dados de qual jogador? (999 para parar) '))
    if dados == 999:
        print('FINALIZANDO... ')
        time.sleep(1)
        break
    elif dados >= len(lista_dic):
        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE... ')
        print('=-'*30)
        for k, v in enumerate(lista_dic):
            print(f'{k:>4} {lista_dic[k]["Nome"]:<22} {str(lista_dic[k]["Gols"]):20} {sum(lista_dic[k]["Gols"]):<20}')
        print('=-'*30)
    else:
        print('=-'*30)
        print(f'- LEVANTAMENTO DO JOGADOR {lista_dic[dados]["Nome"]}')
        for c in range(0, len(lista_dic[dados]['Gols'])):
            print(f'No jogo {c+1} fez {lista_dic[dados]["Gols"][c]} gols')
        print('=-'*30)


