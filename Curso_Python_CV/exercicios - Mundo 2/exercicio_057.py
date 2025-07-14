resp = ''
while resp != 'M' and resp != 'F':
    resp = str(input("Digite seu sexo [M / F]: ")).upper()
    if resp == 'M':
        print('Masculino')
    elif resp == 'F':
        print('Feminino')
    else:
        print('Opção inválida, digite novamente')

print('Acabou')
    
    