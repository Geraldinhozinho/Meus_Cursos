import moeda

dinheiro = float(input('Digite o valor R$'))
print(f'O valor R${moeda.moeda(dinheiro)} com um aumento de 10% é: {moeda.aumentar(dinheiro,10, True)}')
print(f'O valor R${moeda.moeda(dinheiro)} com um diminuimento de 10% é: {moeda.diminuir(dinheiro, 10, True)}')
print(f'O valor R${moeda.moeda(dinheiro)} dobrado é: {moeda.dobro(dinheiro, True)}')
print(f'O valor R${moeda.moeda(dinheiro)} dividido por 2 é: {moeda.metade(dinheiro, False)}')
 