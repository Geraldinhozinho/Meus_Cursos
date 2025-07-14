import termcolor, emoji
valor1 = int(input('digite um valor: '.capitalize()))
valor2 = int(input('digite mais um valor: '.capitalize()))
opcao = ''
while opcao != 5:
    
    print(10*'-','agora escolha uma opção'.capitalize(),10*'-')
    print('[ 1 ] - somar'.upper())
    print('[ 2 ] - multiplicar'.upper())
    print('[ 3 ] - maior'.upper())
    print('[ 4 ] - novos números'.upper())
    print('[ 5 ] - sair do programa'.upper())
    opcao = int(input('digite: '.capitalize()))
    if opcao == 1:
        print('a soma do valor1 ({}) + o valor2 ({}) é igual a: {}'.format(valor1, valor2, valor1+valor2).capitalize())
    elif opcao == 2:
        print('a multiplicação do valor1 ({}) * o valor2 ({}) é igual a: {}'.format(valor1, valor2, valor1*valor2).capitalize())
    elif opcao == 3:
        if valor1 > valor2:
            print('o maior valor entre  valor1 ({}) e valor2 ({}) é : {}'.format(valor1, valor2, valor1).capitalize())
        if valor2 > valor1:
            print('o maior valor entre  valor1 ({}) e valor2 ({}) é : {}'.format(valor1, valor2, valor2).capitalize())
        if valor1 == valor2:
            print('não há maior valor entre  valor1 ({}) e valor2 ({}) amobos são iguais : {}'.format(valor1, valor1, valor1).capitalize())
    elif opcao == 4:
        print('digite os novos valores: '.capitalize())
        valor1 = int(input('digite um valor: '.capitalize()))
        valor2 = int(input('digite mais um valor: '.capitalize()))
        
    elif opcao == 5:
        print('você saiu'.capitalize())
    else:
        print('OPÇÃO INVALIDA')