
import random
tupla = ()
cont = menor = maior = 0
for c in range(0,5):
    a = random.randint(0,10)
    tupla = tupla + (a,)
    if cont == 0:
        maior = a
        menor = a
    else:
        if a > maior:
            maior = a
        if a < menor:
            menor = a
    cont = cont + 1
cont2 = 0
for c in tupla:
    if cont2 < 4:
        print(c, end=' ')
        cont2 = cont2 + 1
    else:
        print(c)

print(f'O maior é: {maior}')
print(f'O menor é: {menor}')