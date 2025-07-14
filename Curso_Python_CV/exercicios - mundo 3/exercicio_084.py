lista = []
dados = []
maispeso = menospeso = 0
while True:
    Nome = str(input('Digite seu nome: '))
    Peso = float(input('Digite seu peso: '))
    dados.append(Nome)
    dados.append(Peso)
    lista.append(dados[:])
    dados.clear()
    
    
    continua = ''
    while continua not in ('S', 'N'):
        continua = str(input('Deseja continuar? [S/N]-> ').upper())
        if continua != 'S' and continua != 'N':
            print('Tente nocamente... ',end=' ')
    if continua == 'N':
        break

print(f'foram cadastradas {len(lista)} pessoas')


for cont, valores in enumerate(lista):
    if cont == 0:
        maispeso = lista[0][1]
        menospeso = lista[0][1]
        
    else:
        if lista[cont][1] > maispeso:
            maispeso = lista[cont][1]
        if lista[cont][1] < menospeso:
            menospeso = lista[cont][1]
print(f'O maior peso foi {maispeso:.2f}KG de: ',end='')
for cont, valores in enumerate(lista):
    if lista[cont][1] == maispeso:
        print(valores[0], end=' ')
print(f'\nO menor peso foi {menospeso:.2f}KG de: ',end='')
for cont, valores in enumerate(lista):
    if lista[cont][1] == menospeso:
        print(valores[0], end=' ')

