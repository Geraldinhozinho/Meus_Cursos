lista = [[],[],[]]
col = lin = soma = somaT = maior =0

for c in range(1,10):
    valor = int(input(f'Digite o valor para a matriz na posição [{lin} , {col}]: '))
    if c <= 3:
        lista[0].append(valor)
    elif 4 <= c < 7:
        lista[1].append(valor)
    else:
        lista[2].append(valor)
        
    col = col + 1
    if c%3 == 0:
        lin = lin + 1
        col = 0
        
print('-=' * 20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{lista[l][c]:^8}]',end= ' ')
    print()
    
