from lib.interface.code import *
from lib.arquivo.code import *
import time

arq = 'Arquivo_nomes'

if Arquivoexiste(arq) == False:
    Criararquivo(arq) 


while True:
    escolha = menu (['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema', 'Limpar Arquivo'])
    if escolha == 1:
        Lerarquivo(arq)
    elif escolha == 2:
        cabeçalho('Cadastrar pessoa'.upper())
        nome = cadastro_nome('Informe o nome da pessoa: ')
        idade = leiaInt('Digite a idade da pessoa: ')
        Cadastrar_pessoa(arq, nome, idade)
    elif escolha == 3:
        cabeçalho('Opção 3'.upper())
        print('Saindo do sistema...') 
        time.sleep(1)
        print('Até logo!')
        break
    elif escolha == 4:
        cabeçalho('Limpando Arquivo'.upper())
        print('Aguarde...'.center(42))
        Limpar_arquivo(arq)
        time.sleep(2)
        print('\033[1;32mFinalizado, arquivo limpo com sucesso\033[m')
    else:
        print('\033[1;31mERRO! digite uma opção válida\033[m')