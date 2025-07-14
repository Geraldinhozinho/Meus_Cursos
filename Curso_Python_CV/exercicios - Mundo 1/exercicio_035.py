Valor1 = int(input('Digite uma reta: '))
Valor2 = int(input('Digite uma reta: '))
Valor3 = int(input('Digite uma reta: '))

if (Valor1 - Valor2) < Valor3 < (Valor1 + Valor2):
    print(True, ',É um triângulo')
else:
    print(False, ',Não é um triângulo')

