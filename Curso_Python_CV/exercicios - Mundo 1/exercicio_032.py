import datetime, termcolor
Ano = int(input('Qual o ano que deseja verificar? ' + termcolor.colored('Digite 0 para verificar o ano atual ','green')))

if Ano == 0:
    Ano = datetime.date.today().year
if Ano % 4 == 0 and Ano % 100 != 0 or Ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(Ano))
else:
    print('O ano {} não é BISSEXTO'.format(Ano))