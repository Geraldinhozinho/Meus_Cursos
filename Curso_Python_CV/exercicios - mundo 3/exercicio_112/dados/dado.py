def leiaDinheiro(msg):
    valido = False
    valor = 0
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha():
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
            print(f'\033[1;31m<{entrada}> NÃO É VÁLIDO\033[m')
        else:
            valido = True
            return float(entrada)
    return valor