import termcolor, time
Valorcasa = float(input('\033[1;37mQual o valor da casa? '))
Valorsalario = float(input('Qual o valor do seu salário? '))
Anos = int(input('Em quantos anos você planeja pagar essa dívida? '))
print('\033[m')

Valorsalario_novo = Valorsalario - (Valorsalario * 70 / 100)
Parcela = (Valorcasa / (12 * Anos))

if Parcela > Valorsalario_novo:
    print('Você não pode comprar essa casa no valor de {} R$. \nO valor da parcela é {} R$ em {} anos'.format(termcolor.colored(f'{Valorcasa:.2f}','yellow'),termcolor.colored(f'{Parcela:.2f}', 'red'), Anos))
    print('\033[1;31mEMPRESTIMO NEGADO...')
else:
    print('Você pode comprar essa casa no valor de {} R$. \nO valor da parcela é {} R$ em {} anos'.format(termcolor.colored(f'{Valorcasa:.2f}','yellow'),termcolor.colored(f'{Parcela:.2f}', 'green'), Anos))
    print('\033[1;32mEMPRESTIMO APROVADO...')
    
print('\033[m')

print('\033[1;32mCOMPARANDO...\033[m')
time.sleep(2)
print('Os 30% do seu salário é {} R$ e a parcela é {} R$ '.format(termcolor.colored(f'{Valorsalario_novo:.2f}','green'),termcolor.colored(f'{Parcela:.2f}','red')))