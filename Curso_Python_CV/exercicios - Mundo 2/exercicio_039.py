import datetime

Ano = int(input('\033[4;1;36mInforme o nome do seu nascimento: '))

print('\033[m')
Ano_atual = datetime.date.today().year
Idade = Ano_atual - Ano 
print('Sua idade é: {} anos'.format(Idade))
if Idade == 18:
    print('\033[1;32mVocê está na idade de se alistar, você possui {} Anos de idade. Aguardo você. \033[m'.format(Idade))
elif Idade < 18:
    print('\033[1;37mAinda falta um pouco para você se alistar, cerca de {} Ano(s). Estou Aguardando você em {}. \033[m'.format(18 - Idade, (18 - Idade)+Ano_atual))
else:
    print('\033[1;31mJá passou do período de alistamento, cerca de {} Ano(s) atrás o ano do seu alistamento era {}. Estou Aguardando você. \033[m'.format(Idade - 18, Ano_atual-(Idade - 18)))