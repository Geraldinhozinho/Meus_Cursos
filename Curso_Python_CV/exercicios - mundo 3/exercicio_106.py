import time, random

cores = (
    '\033[m',
    '\033[1;30;40m',
    '\033[1;30;41m',
    '\033[1;30;42m',
    '\033[1;30;43m',
    '\033[1;30;44m',
    '\033[1;30;45m',
    '\033[1;30;46m',
    '\033[1;30;47m',
)
def sistema(com):
    tam = len(com) + 35
    print(f'{cores[5]}')
    print('~' * tam)
    print(f'  Acessando o manual do comando: {com}')
    print('~' * tam, end='')
    
    def ajuda():
        print(f'{x}')
        help(com)
        time.sleep(1)
    ajuda()

comando = ''
while True:
    print('\033[1;30;42m')
    print('~'*27)
    print('  Sistema de ajuda PYhelp')
    print('~'*27,'\033[m')
    
    comando = str(input('Função ou Biblioteca: ')).lower().strip()
    if comando == 'fim':
        break
    cor = random.randint(0,8)
    x = cores[cor]
    sistema(comando)
    
print('\033[1;30;41m')
print('~'*12)
print('  Até logo')
print('~'*12,'\033[m')
