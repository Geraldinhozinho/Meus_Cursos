Nome = str(input('Digite o seu nome : ')).strip()
Nome = Nome.split()

print( 'Olá {}, parabéns.'.format(Nome[0]))
print( 'Seu primeiro nome é: {}, parabéns.'.format(Nome[0]))
print( 'Seu último nome é: {}, parabéns.'.format(Nome[-1]))
