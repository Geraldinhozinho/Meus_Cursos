
idades= 0
maior = 0
mulheres = 0
mulheres18 = 0
nomeh = None
for c in range(1,3):
    print('\033[1;31mRodada {}'.format(c))
    nome = str(input('\033[1;32mDigite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M / F]: ').upper())
    print(20*'==','\033[m')
    idades += idade 

    if idade > maior and sexo == 'M':
        maior = idade
        nomeh = nome
         
    elif sexo == 'F'and idade < 20:
        mulheres += 1
        
    elif sexo == 'F'and idade >= 20:
        mulheres18 += 1
media = idades/4
print('\033[1;33mA média das idades do grupo é: {}'.format(media))
if maior == 0:
    print('\033[1;31mNão há homens na listagem')
else:
    print('\033[1;33mO mais velho é: \033[1;37m',nomeh,'\033[1;33m e a idade é: \033[1;37m', idade)
if mulheres == 0:
    print('\033[1;31mNão há mulheres na listagem')
else:
    print('\033[1;37m',mulheres,'\033[1;33m Mulheres com menos de 20 anos')
    print('\033[1;37m',mulheres18,'\033[1;33m Mulheres com mais de 19 anos')

    