gasto =  baratonome = caro = 0
barato = 0
con = 1
print(10*'-','bem-vindo ao  barateiro'.upper(),10*'-')

while True:
    Nomep = str(input('Digite o nome do produto: '.upper()).upper())
    Valorp = float(input('Digite o preço do produto: R$ '.upper()).upper())
    gasto = gasto + Valorp
    
    if Valorp > -1 and con ==1:
        print('Obrigado!1')
        barato = Valorp
        baratonome = Nomep 
        con = con + 1 
    
    if Valorp < barato :
        print('Obrigado!2')
        barato = Valorp
        baratonome = Nomep
        con = con + 1
       
    if Valorp > 1000:
        caro = caro +1 
        con = con + 1
    
    if Valorp <= 1000 and con > 2 and Valorp > barato: 
        con = con + 1
    
    continua = ''
    while continua not in ('S', 'N'):
        print('a')
        continua = input('Deseja comprar mais? [S / N]: ').strip().upper()

    if continua == 'N':
        break


print(f'''
foi gasto no total {gasto:.2f}
houve {caro} produtos custando mais de 1000R$
o produto mais barato foi {baratonome} no valor de {barato:.2f}     
''')

