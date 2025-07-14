import random, time, operator
dic = {'Jogador1': random.randint(1,6),
       'Jogador2': random.randint(1,6),
       'Jogador3': random.randint(1,6),
       'Jogador4': random.randint(1,6),}
lista = []
for k, v in dic.items():
    print(f'{k} tirou {v}')
    time.sleep(1)
lista = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
for j, r in enumerate(lista):
    print(f'{j+1}º LUGAR foi o {r[0]} que tirou {r[1]}')
    time.sleep(1)