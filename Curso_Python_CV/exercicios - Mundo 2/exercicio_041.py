from datetime import date
import termcolor
Ano = int(input('\033[1;32mDigite o ano do seu nascimento: '))
print('\033[1;31m',12*'-=-','\033[m')
Ano_atual = date.today().year
Idade =  Ano_atual - Ano

if Idade <= 9:
    print('\033[1;37mVocê é da categoria \033[1;32mMirim\033[m')
elif Idade <= 14:
    print('\033[1;37mVocê é da categoria \033[1;34mInfantil\033[m')
elif Idade <= 19:
    print('\033[1;37mVocê é da categoria \033[1;33mJunior\033[m')
elif Idade <= 20:
    print('\033[1;37mVocê é da categoria \033[1;36mSênior\033[m')
else:
    print('\033[1;37mVocê é da categoria \033[1;35mMaster\033[m')
    
print('\033[1;37mSua idade é: \033[m{}'.format(termcolor.colored(Idade,'yellow')))

    