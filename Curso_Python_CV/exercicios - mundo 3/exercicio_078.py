



maior = menor = 0
lista = []

for c in range(0,5):
    v1=  int(input(f'Valor {c+1} na posição {c}: '))
    lista.append(v1)
    if c == 0:
        maior = v1
        menor = v1
    else:
        if v1 > maior:
            maior = v1                
        if v1 < menor:
            menor = v1
    
print(f'Os valores foram: {lista}')
print(f'O maior valor foi {maior} e está nas posições: ',end=' ')

for posicao , valor in enumerate(lista):
    if valor == maior:
        print(posicao, end=' ')
        
print(f'\nO menor valor é {menor} e está nas posições: ',end=' ')
for posicao , valor in enumerate(lista):
    if valor == menor:
        print(posicao, end=' ')
        
