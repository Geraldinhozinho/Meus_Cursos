Distancia = float(input('\033[1;34mQual a distancia percorrida: \033[m'))
Dias = float(input('\033[1;35mQuantos dias você usou o carro?  \033[m'))

resultado = (Distancia * 0.15) + (Dias * 60)

print('\033[1;33mO total a pagar é: \033[1;31m{:.2f} R$\033[m'.format(resultado))