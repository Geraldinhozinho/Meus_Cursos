import termcolor
Velocidade = float(input('Digite a velocidade do carro: '))
if Velocidade > 80:
    print(termcolor.colored('Você foi multado','red'))
    print (termcolor.colored('o valor da multa é: {}'.format((Velocidade - 80)*7),'green'))
else:
    print('Você está dirigindo no limite aceito. PARABÉNS')