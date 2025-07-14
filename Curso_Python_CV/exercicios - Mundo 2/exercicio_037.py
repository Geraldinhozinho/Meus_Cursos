Valor = int(input('\033[1;33mDigite um número: '))
print('\033[mAgora escolha uma opção:')
print('\033[1;32m[ 1 ] Para converter o valor {} em Binário'.format(Valor))
print('[ 2 ] Para converter o valor {} em Octal'.format(Valor))
print('[ 3 ] Para converter o valor {} em Hexadecimal'.format(Valor))
Opcao = int(input('Digite sua Opção: '))
print('\033[m')
if Opcao == 1:
    print('\033[1;31mO número {} em Binário é: {}\033[m'.format(Valor,bin(Valor)[2:]))
elif Opcao == 2:
    print('\033[1;31mO número {} em Octal é: {}\033[m'.format(Valor,oct(Valor)[2:]))
elif Opcao == 3:
    print('\033[1;31mO número {} em Hexadecimal é: {}\033[m'.format(Valor,hex(Valor)[2:].upper()))
else:
    print('\033[1;31mOpção errada')