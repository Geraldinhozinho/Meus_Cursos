soma = 0
contador = 0
num = ' '
a = 1
while num != 999:
    num = int(input('Digite o {}º número: '.format(a)))
    if num != 999:
        soma = soma + num
        contador = contador + 1
        a = a + 1
print('Números digitados: {}'.format(contador))
print('Números somados: {}'.format(soma))
