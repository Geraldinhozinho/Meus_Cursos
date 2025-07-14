

contador18 = contadorH = contadorM = tudo= 0


while True:
    idade = int(input('Digite sua idade: '))
    while True:
        sexo = str(input('Digite seu sexo [M / F]: ').upper())[0]
        if sexo == 'M' or sexo == 'F':
            break  # Se a resposta for válida, sai do laço
        else:
            print('APENAS M ou F. Tente novamente.')
    if idade > 18 and sexo == 'M':
        contadorH = contadorH + 1
        contador18 = contador18 + 1
        tudo = tudo + 1
    
    elif idade <= 18 and sexo == 'M':
        contadorH = contadorH + 1
        tudo = tudo + 1
        
    elif idade > 19:
        contador18 = contador18 + 1
        tudo = tudo + 1

    elif idade >= 18 < 20 and sexo == 'F':
        contadorM = contadorM + 1
        contador18 = contador18 + 1
        tudo = tudo + 1
    elif idade < 18 and sexo == 'F':
        contadorM = contadorM + 1
        tudo = tudo + 1
        
    continua = str(input('Continua [S / N]: ').upper())[0]
    if continua == 'N':
        break
    # Caso a resposta não seja 'N', verifica se é 'S', senão pede novamente
    while continua != 'S' and continua != 'N':
        print('Opção inválida. Por favor, digite apenas S ou N.')
        continua = str(input('Continua [S / N]: ').upper())[0]
print(
f'''ACABOU...
foram cadastrados {tudo} ao todo
foram cadastrados {contador18} pessoas com mais de 18 anos
foram cadastrados {contadorH} Homens
foram cadastrados {contadorM} Mulheres com menos de 20 anos

''')