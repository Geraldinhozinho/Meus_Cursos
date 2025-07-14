n = int(input('digite: '.capitalize()))
contador = 3
F1 = 0 
F2 = 1
print('{} → {} → '.format(F1, F2), end='')
while contador < n:
    F3 = F1 +  F2
    print('{} → '.format(F3), end='')
    F1 = F2
    F2 = F3
    contador = contador + 1

print('FIM')
    
    
    #     temp = (F1) = 0
    #     F1 = (F2) = 1
    #     F2 = 0 + 1