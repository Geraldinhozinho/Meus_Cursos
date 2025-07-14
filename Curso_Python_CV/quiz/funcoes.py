import time

perguntas = [
    '1) Qual é o nome completo do Naruto? ',
    '2) Quem é o sensei do time 7? ',
    '3) Qual é o clã do Sasuke? ',
    '4) Qual o nome da raposa nove caudas?',
    '5) Qual técnica é famosa do Kakashi? '
]

alternativas = [
    'A) Naruto Uchiha  B) Naruto Hatake  C) Naruto Uzumaki  D) Naruto Hyuuga',
    'A) Kakashi  B) Iruka  C) Asuma  D) Gai',
    'A) Uzumaki  B) Hyuuga  C) Nara  D) Uchiha',
    'A) Bijuu  B) Kurama  C) Shukaku  D) Kyubi',
    'A) Rasengan  B) Byakugan  C) Chidori  D) Sharingan'
]

respostas = ['c', 'a', 'd', 'b', 'c']


def cabeçalho(txt):
    linha()    
    print(txt.center(42))
    linha()

def linha( tam = 42):
    print(tam * '-')
def verificando():
    print('Verificando... Aguarde')
    time.sleep(0)
    
    

def rpt(valor):
    print(f'\033[1;34m{valor}\033[m'.center(42))
    linha()
    
def acertou(tex, tam = 42):
    print(tam * '*')
    print(f'\033[1;32m{tex.center(42)}\033[m')
    print(tam * '*')
    
def errou(tex, tam = 42):
    print(tam * '*')
    print(f'\033[1;31m{tex.center(42)}\033[m')
    print(tam * '*')

def resp_certa(valor):
    print(f'\033[1;37;40m  A resposta correta era: opção {valor}  \033[m')
    
    
contador = 0
def resposta(perg):
    import time
    global contador
    acertos = 0
    erros = 0
    for p in perguntas:
        cabeçalho('Quiz do Naruto')
        rpt(f'{p}')
        for alt in alternativas[contador].split('  '):
            print(alt)
        linha()
        resp = str(input(perg))
        if resp == respostas [contador]:
            verificando()
            acertou('Acertou!!!')
            acertos = acertos + 1
            if resp != respostas [contador]:
                verificando()
                errou('Errou')
                resp_certa(respostas[contador].upper())
                erros = erros + 1
        else:
            while resp.isnumeric() == True or resp not in respostas:
                cabeçalho('Quiz do Naruto')
                rpt(p)
                for alt in alternativas[contador].split('  '):
                    print(alt)
                linha()
                print('\033[1;31mOPS... Não há essa opção, tente novamente\033[m')
                resp = str(input(perg))
            if resp == respostas [contador]:
                verificando()
                acertou('Acertou!!!')
                acertos = acertos + 1
            else:
                verificando()
                errou('Errou')
                resp_certa(respostas[contador].upper())
                erros = erros + 1
        contador = contador + 1
    print('Calculando pontuação...'.upper())
    time.sleep(2)
    import termcolor
    linha()
    print(termcolor.colored(f'Parabéns, você acertou {acertos} perguntas!!! '.upper(), 'blue'))
    linha()
    print(termcolor.colored(f'Poxa, você errou {erros} perguntas!!! '.upper(),'red'))
    linha()
