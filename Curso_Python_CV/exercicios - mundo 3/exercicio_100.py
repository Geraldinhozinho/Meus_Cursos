import random
números = []
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0,5):
        sorteio = random.randint(0,20)
        lista.append(sorteio)
        print(f'{sorteio} ', end='')
    print('Pronto!'.upper())

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma = soma + valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

sorteia(números)
somapar(números)