
maior = 0
menor = 0
for c in range(1, 7):
    peso = float(input('Digite o peso {}: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print('{} é o maior peso '.format(maior))
print('{} é o menor peso '.format(menor))