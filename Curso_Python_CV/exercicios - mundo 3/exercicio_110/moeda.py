def aumentar(valor, taxa, form = False):
    if form == False:
        aumento = valor + ((valor * taxa) /100)
        return aumento
    else:
        aumento = valor + ((valor * taxa) /100)
        return moeda(aumento)
    
def diminuir(valor, taxa, form = False):
    if form == False:
        diminui = valor - ((valor * taxa) / 100)
        return diminui
    else:
        diminui = valor - ((valor * taxa) / 100)
        return moeda(diminui)
      
def dobro(valor, form = False):
    if form == False:
        multiplica = valor * 2
        return multiplica
    else:
        multiplica = valor * 2
        return moeda(multiplica)
    
def metade(valor, form = False):
    if form == False:
        metade = valor / 2
        return metade
    else:
        metade = valor / 2
        return moeda(metade)
    
def moeda(valor= 0, moeda = 'R$'):
    moeda = (f'{moeda}{valor:.2f}'.replace('.',','))
    return moeda 
 
def resumo(valor = 0, taxa = 10, taxar = 5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{taxa}% de aumento: \t{aumentar(valor, taxa, True)}')
    print(f'{taxa}% de redução: \t{diminuir(valor, taxar, True)}')
    print('-'*30)
    
    
    
    