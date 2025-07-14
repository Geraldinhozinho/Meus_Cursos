

      
tupla = (
int(input('digite um valor: ').capitalize()),    
int(input('digite outro valor: ').capitalize()),   
int(input('digite mais um valor: ').capitalize()),    
int(input('digite o último valor: ').capitalize())
)
print(f'valores: {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
a = tupla.count(3)
if a > 0:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
else:
    print(f'O valor 3 não apareceu em nenhuma posição')
       

    
print(f'Os valores pares digitados foram: ',end='')
for cont in tupla:
    if cont % 2 ==0:
        print(cont, end=' ')
    else:
        print('',end='')