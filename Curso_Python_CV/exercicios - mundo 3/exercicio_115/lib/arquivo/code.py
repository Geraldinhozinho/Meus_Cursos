from lib.interface.code import *


def Arquivoexiste(nome):
    try: 
        a = open(nome, 'rt')
        a.close()
    except:
        print('\033[1;31mOcorreu um ERRO o arquivo não existe\033[m')
        return False
    else:
        print('\033[1;32mO arquivo existe\033[m')
        return True
    
def Criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[1;31mOcorreu um ERRO ao criar o arquivo\033[m')
    else:
        print(f'\033[1;32mO arquivo {nome} foi criado com sucesso\033[m')
        
        
def Lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[1;31mOcorreu um ERRO ao ler o arquivo\033[m')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')
        
        
    finally:
        a.close()
def Cadastrar_pessoa(arq, nome , idade):
    try:
        a = open(arq, 'at')
    except:
        print('\033[1;31mOcorreu um ERRO ao abrir o arquivo\033[m')
    else:
        try:
            a.write(f'{nome}; {idade}\n')   
        except:
            print('\033[1;31mOcorreu um ERRO ao escrever no arquivo\033[m')
        else:
            print('\033[1;32mSECESSO escrever no arquivo\033[m')
            a.close()
            
          
def Limpar_arquivo(nome):
    a = open(nome, 'w')  
    a.truncate(0)
    a.close()
    return a
