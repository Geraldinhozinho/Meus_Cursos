lista = [[],[]]
for valor in range(1,8):
    valor = int(input(f'Digite o {valor}º valor: '))
    if valor%2 == 0:
        lista[0].append(valor)
    if valor%2 == 1:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print('Os valores pares são: ',lista[0])
print('Os valores pares são: ',lista[1])



