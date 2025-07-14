
print('\033[1;30;42m======Desafios da aula 06 ======\033[m')


print('\033[1;30;45m======Desafio 03 ======\033[m')
N1=int(input('\033[1;30;45mDigite um valor: \033[m'))
N2=int(input('\033[1;30;45mDigite um segundo valor: \033[m'))
Soma1=N1+N2

N3=float(input('\033[1;30;46mDigite um valor: \033[m'))
N4=float(input('\033[1;30;46mDigite um segundo valor:\033[m'))
Soma2=N3+N4

N5=bool(input('\033[1;30;47mDigite um valor: \033[m'))
N6=bool(input('\033[1;30;47mDigite um segundo valor: \033[m'))
Soma3=N5,N6

N7=str(input('\033[1;30;42mDigite um valor: \033[m'))
N8=str(input('\033[1;30;42mDigite um segundo valor: \033[m'))
Soma4=N7+N8

print('\033[4;36;40mA soma do números int é: {} \033[m'.format(Soma1))
print('\033[4;36;40mA soma do números float é: {} \033[m'.format(Soma2))
print('\033[4;36;40mA soma do números bool é: {} \033[m'.format(Soma3))
print('\033[4;36;40mA soma do números str é: {} \033[m'.format(Soma4))



print('======Desafio 04 ======')

A1 = (input('\033[7;36;40mDigite um valor: '))
print(A1.isnumeric())
print(A1.isalpha())
print(A1.isalnum())