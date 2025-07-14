def ficha(jog = '< Desconhecido >', gol = 0):
    
    print(f'O jogador {jog} fez um total de {gol} durante a partida')



print('-'*20)
n = str(input('Digite o nome do jogador: '))   
g = str(input('Quantos gols na partida o Jogador fez: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else: 
    ficha(n, g)