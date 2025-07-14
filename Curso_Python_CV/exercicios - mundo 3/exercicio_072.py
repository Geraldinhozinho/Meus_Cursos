tupla = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
    "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
)
while True:
    while True:
        valor = int(input(' digite um valor entre 0 e 20: '.upper()).upper())
        if valor < 21 and valor > -1:
            print('você digitou o número'.upper(),f'\033[1;32m{tupla[valor].upper()}\033[m')
            break
        print('tente novamente... '.upper(),end='')
        
    continua = ''
    while continua not in ('S', 'N'):
        
        continua = input('Deseja comprar mais? [S / N]: ').strip().upper()
        if continua != 'S' and continua != 'N':
            print('tente novamente... '.upper(),end='')
            
    if continua == 'N':
        break
    

# import termcolor
# nome = 'geraldo'.upper()

# print(termcolor.colored('meu'.upper(),'red'),'nome é {}'.upper().format(termcolor.colored(nome,'green')))
# print('a'.upper()) 