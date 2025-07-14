
def num(* valores):
    maior = 0
    print('Analisando os valores passados: ')
    for c in valores:
        print(c, end=' ')
        if c > maior:
            maior = c
    print(f'Foram informados {len(valores)} valores ao todo')
    print(f'O maior valor é: {maior}')
    print('-=' * 20) 
print('-=' * 20)    
num(1,22,3,4,55)
num(1,5)
num()
num(1,5,3,4,5,6,3,2,1,1,1,1,2,5)