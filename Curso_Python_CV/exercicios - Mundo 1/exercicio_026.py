Nome = str(input('\033[1;32;40mDigite o seu nome : \033[m')).strip().upper()
Nome = Nome.replace('Á','A').replace('Â','A').replace('Ã','A')

print( '\033[1;35mSeu nome possui a letra A, {} vezes parabéns.'.format(Nome.count('A')))
print( 'Seu nome possui a letra A, e ela apareceu primeiro na posição {}, parabéns.'.format(Nome.find('A')+1))
print( 'Seu nome possui a letra A, e ela apareceu pela última vez na posição {}, parabéns.\033[m'.format(Nome.rfind('A')+1))
