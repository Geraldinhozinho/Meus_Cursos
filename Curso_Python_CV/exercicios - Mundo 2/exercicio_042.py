import termcolor
Valor1 = int(input('\033[1;32mDigite uma reta: '))
Valor2 = int(input('Digite outra reta: '))
Valor3 = int(input('Digite mais uma reta: '))
print(15*'-=-','\033[m')
Condicao = (Valor1 - Valor2) < Valor3 < (Valor1 + Valor2)
if Condicao == True and Valor1 == Valor2 and Valor1 == Valor3 and Valor2 == Valor3:
    print(termcolor.colored(True,'green'), termcolor.colored(',É um triângulo e ele é do tipo Equilátero','blue'))
elif Condicao == True and Valor1 == Valor2 or Valor1 == Valor3 or Valor2 == Valor3:
    print(termcolor.colored(True,'green'), termcolor.colored(',É um triângulo e ele é do tipo Isóceles ','blue'))
elif Condicao == True and Valor1 != Valor2 and Valor1 != Valor3 and Valor2 != Valor3:
    print(termcolor.colored(True,'green'), termcolor.colored(',É um triângulo e ele é do tipo Escaleno ','blue'))
else:
    print(termcolor.colored(False,'red'), termcolor.colored(',Não é um triângulo','yellow'))