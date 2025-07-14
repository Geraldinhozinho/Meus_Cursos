def aumentar(valor, taxa):
    aumento = valor + ((valor * taxa) /100)
    return aumento
    
def diminuir(valor, taxa):
    diminui = valor - ((valor * taxa) / 100)
    return diminui
      
def dobro(valor):
    multiplica = valor * 2
    return multiplica
    
def metade(valor):
    metade = valor / 2
    return metade


def moeda(valor= 0, moeda = 'R$'):
    moeda = (f'{moeda}{valor:.2f}'.replace('.',','))
    return moeda 