def voto(ano):
    """FUNÇÃO VOTO

    Args:
        ano (INT): É O ANO DE NASCIMENTO DO USUÁRIO
    """
    import datetime
    ano_atual = datetime.date.today().year
    idade = ano_atual - ano
    if 16 <= idade < 18 or idade > 65 :
        return f'Você tem {idade} anos. o voto é OPCIONAL!'
    elif  idade >= 18:
        return f'Você tem {idade} anos. o voto é OBRIGATÓRIO!'
    else:
        return f'Você tem {idade} anos. o voto é PROIBIDO!'
    
print('-'*25)
ano = int(input('Qual seu ano de nascimento? '))

x = voto(ano)
print(x)
if len(x) > 10:
    print('oi')