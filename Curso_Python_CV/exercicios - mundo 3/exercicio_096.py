def area(comprimento, largura):
    area = comprimento * largura 
    print(f'A área total é {area} m²')

    

print(30*'-')
largura = float(input('Digite a largura do terreno: '))
comprimento  = float(input('Digite o Comprimento do terreno: '))
area(comprimento, largura)
