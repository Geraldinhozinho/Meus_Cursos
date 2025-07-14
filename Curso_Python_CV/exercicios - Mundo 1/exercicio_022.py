Nome = input('Digite um nome completo: ')


Maiuscula = Nome.upper().strip()
Minuscula = Nome.lower().split()
espacos = Nome.strip()
contar = Nome.split()

print('\033[1;44mNome maiúsculo: {}\033[m'.format(Maiuscula))
print('\033[1;41mNome minúculo: {}\033[m'.format(Minuscula))
print('\033[1;42mQuantidade de letras sem espaços: {}\033[m'.format(len(espacos) - espacos.count(' ')))
print('\033[1;43mQuantidade de letras no primeiro nome: {} {}\033[m'.format(contar[0],len(contar[0])))
