# def notas(* notas, sit = False):
#     """
#     -> Função para analisar notas e situações de vários alunos.
#     :param n: uma ou mais notas (aceita várias)
#     :param situação: (opcional), indica se deve ou não mostrar a situação do aluno.
#     :return: dicionário com várias informações sobre a situação da turma.
#     """
#     dicionario = {}
#     dicionario['Notas:'] = len(notas)
#     dicionario['Maior:'] = max(notas)
#     dicionario['Menor:'] = min(notas)
#     dicionario['Média:'] = sum(notas)/len(notas)
#     if sit == True:
#         if dicionario['Média:'] >= 7:
#             dicionario['Situação:'] = 'BOA'
#         elif dicionario['Média:'] <= 6.9:
#             dicionario['Situação:'] = 'Razoável'
#         else:
#             dicionario['Situação:'] = 'Ruim'


#     a = dicionario
#     return a
    
# resultado = notas(1,2,4,5, sit=True)
# print(resultado)

def notas(* notas, sit = False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas (aceita várias)
    :param situação: (opcional), indica se deve ou não mostrar a situação do aluno.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dicionario = {}
    media =  0
    menor = maior = notas[0]
    dicionario['Notas:'] = len(notas)
    for soma in notas:
        media = media + soma
        if soma > maior:
            maior = soma
        if soma < menor:
            menor = soma
            
    dicionario['Menor:'] = menor
    dicionario['Maior:'] = maior       
    dicionario['Média:'] = media/len(notas)
    
    
    
    if sit == True:
        if dicionario['Média:'] >= 7:
            dicionario['Situação:'] = 'BOA'
        elif dicionario['Média:'] <= 6.9:
            dicionario['Situação:'] = 'Razoável'
        else:
            dicionario['Situação:'] = 'Ruim'


    a = dicionario
    return a
    
resultado = notas(1,2,4,5, sit=True)
print(resultado)

