import random
num = random.randint(0, 10)
contador = 0
numuser = ''
print(num)
while num != numuser:
    numuser = int(input('\033[1;37mdigite um valor: '.capitalize())) 
    contador += 1
    if num > numuser:
        print('\033[1;30mmais...'.upper())
        print('\033[1;30mValor inválido, tente novamente')
    elif num < numuser:
        print('\033[1;30mmenos...'.upper())
        print('\033[1;30mValor inválido, tente novamente')
if contador == 1:
    print('\033[1;32mUAU! você ganhou de primeira, só chutou {}x\033[m'.format(contador))
else:   
    print('\033[1;36mVocê ganhou, mas teve que dá {} chutes\033[m'.format(contador))