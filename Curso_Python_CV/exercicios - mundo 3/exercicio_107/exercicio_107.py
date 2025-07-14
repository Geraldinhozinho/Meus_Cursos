import moeda

dinheiro = float(input('Digite o preço R$'))
print(f'O valor R${dinheiro} com um aumento de 10% é: {moeda.aumentar(dinheiro, 10)}')
print(f'O valor R${dinheiro} com um diminuimento de 10% é: {moeda.diminuir(dinheiro,10)}')
print(f'O valor R${dinheiro} dobrado é: {moeda.dobro(dinheiro)}')
print(f'O valor R${dinheiro} dividido por 2 é: {moeda.metade(dinheiro)}')
 