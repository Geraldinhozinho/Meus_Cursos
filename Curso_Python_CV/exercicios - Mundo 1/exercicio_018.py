import math
valor = float(input('\033[1;34mDigite um valor: \033[m'))

Resultado1 = math.cos(math.radians(valor))
Resultado2 = math.sin(math.radians(valor))
Resultado3 = math.tan(math.radians(valor))

print('O coseno é: {:.2}\nO Seno é: {:.2}\nA tangente é:{:.2}'.format(Resultado1,Resultado2,Resultado3))