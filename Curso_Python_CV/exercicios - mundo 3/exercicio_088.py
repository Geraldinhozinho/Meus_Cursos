import random, time
lista = []
jogosfeitos = []
texto= 'Joga na mega sena'
print('-'*40)
print(f'{texto:^40}')
print('-'*40)

jogos = int(input('Digite quantos jogos deverão ser sorteados: '))
print('-='*6, f' Sorteando {jogos} jogos ','-='*6)
time.sleep(1)
for j in range(1, jogos +1):
    for sort in range(1,7):
        while len(lista) < 6:
            sorteio = random.randint(1,60)
            if sorteio not in lista:
                lista.append(sorteio)
            if sorteio in lista:
                while sorteio in lista:
                    sorteio = random.randint(1,60 )
    jogosfeitos.append(lista[:]) 
    lista.sort()
    print(f'Jogo {j}: {lista}')
    lista.clear()
    time.sleep(1)
print('-='*10, f'< Boa Sorte! > ','-='*10)
