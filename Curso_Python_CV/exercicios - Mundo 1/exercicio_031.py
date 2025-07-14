import termcolor
Viagem = float(input('Qual a distancia da viagem? '))

if Viagem <= 200:
    print(termcolor.colored('Sua viagem custará 0.50R$ por KM rodado, isso dá um total de {:.2f} a ser pago. '.format(Viagem*0.50),'green'))
else:
    print('Sua viagem custará 0.45R$ por KM rodado, isso dá um total de {:.2f} a ser pago. '.format(Viagem*0.45))