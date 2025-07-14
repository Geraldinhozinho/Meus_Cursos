from termcolor import colored
Nota1 = float(input('\033[1;37mDigite a primeira nota: '))
Nota2 = float(input('Digite a Segunda nota: '))
print(10*'-=-','\033[m')

Media = (Nota1 + Nota2) / 2

if Media >= 70.0:
    print('\033[1;32mParabéns, você está aprovado! \033[m')
elif Media >= 50 <= 60.9:
    print('\033[1;33mPoxa, que pena, você ficou de recuperação. \033[m')
else:
    print('\033[1;31mIIIIIIIH, você reprvou. \033[m')
    
print(10*'-=-') 
print('\033[1;37mSua nota \033[m{:.2f}'.format(colored(Media,'white','on_green')))