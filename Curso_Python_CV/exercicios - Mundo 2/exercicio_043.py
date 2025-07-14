Nome = input('\033[1;37mOlá, Digite seu nome: ')
Altura = float(input('Digite sua Altura {}: '.format(Nome)))
Peso = float(input('Digite seu peso {}: '.format(Nome)))

IMC = (Peso) / ((Altura/100) * (Altura/100))
print('\033[m')
if IMC < 18.5:
    print('{}, \033[1;36mVocê está abaixo do peso, seu IMC é {:.2f}\033[m'.format(Nome,IMC))
elif IMC < 25:
    print('{}, \033[1;32mVocê está no peso ideal, parabéns, seu IMC é {:.2f}\033[m'.format(Nome,IMC))
elif IMC < 30:
    print('{}, \033[1;33mVocê está acima do peso ideal, sobrepeso, seu IMC é {:.2f}\033[m'.format(Nome,IMC))
elif IMC < 40:
    print('{}, \033[1;35mVocê está acima do peso ideal, obesidade, seu IMC é {:.2f}\033[m'.format(Nome,IMC))
else:
    print('{}, \033[1;31mVocê está muito acima do peso ideal, Obesidade mórbida, seu IMC é {:.2f}\033[m'.format(Nome,IMC))