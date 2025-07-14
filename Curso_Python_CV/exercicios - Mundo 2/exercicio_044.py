from termcolor import colored
print(colored('{:-^80}','red').format(colored('------ Olá seja bem vindo a nossa loja ------','green')))
Produto = float(input('\033[1;37mDigite o valor do produto comprado: '))
print(colored('------Agora selecione a forma de pagamento------','green'))
print('\033[1;33m[ 1 ]\033[1;34m Para pagar à vista com dinheiro ou cheque e ganhar 10% de desconto')
print('\033[1;33m[ 2 ]\033[1;34m Para pagar à vista no cartão de crédito e ganhar 5% de desconto')
print('\033[1;33m[ 3 ]\033[1;34m Para pagar em até 2x no cartão o preço normal permanece')
print('\033[1;33m[ 4 ]\033[1;34m Para pagar em 3x ou mais no cartão de crédito e sofrer juros de 20% \033[m')
Opcao = int(input('\033[1;37mSelecione a opção: '))
Desconto = Produto - (Produto * 10 / 100)
Desconto_cartao = Produto - (Produto * 5 / 100)
Juros = Produto + (Produto * 20 / 100)

if Opcao == 1:
    print('\033[1;32mÓtimo, você pagará à vista no dinheiro ou cheque e ganhará \033[1;33m10% de desconto\033[1;32m, o produto que custava \033[1;31m{:.2f} R$\033[1;32m, agora custará \033[1;34m{:.2f} R$\033[m'.format(Produto,Desconto))
elif Opcao == 2:
    print('\033[1;35mÓtimo, você pagará à vista no cartão de crédito e ganhará \033[1;33m5% de desconto\033[1;35m, o produto que custava \033[1;31m{:.2f} R$\033[1;35m, agora custará \033[1;32m{:.2f} R$\033[m'.format(Produto, Desconto_cartao))
elif Opcao == 3:
    print('\033[1;33mÓtimo, você pagará em 2x no cartão, o produto continua custando o mesmo valor \033[1;34m{:.2f} R$\033[1;33m, em 2x fica \033[1;32m{:.2f} R$\033[1;33m cada parcela\033[m'.format(Produto,Produto/2))
elif Opcao == 4:
    print('\033[1;37mVocê pagará em 3x vezes ou mais no cartão')
    parcelas = int(input('Digite o número de parcela: '))
    print('\033[1;34mÓtimo, você pagará em \033[1;33m{}x\033[1;34m, o produto que custava \033[1;31m{:.2f} R$\033[1;34m, agora custará \033[1;33m{:.2f} R$\033[1;34m, devido os juros e cada parcela fica no valor de \033[1;31m{:.2f}R$\033[m'.format(parcelas,Produto,Juros,Juros/parcelas))
else:
    print('\033[1;31mOpção invalida\033[m')
