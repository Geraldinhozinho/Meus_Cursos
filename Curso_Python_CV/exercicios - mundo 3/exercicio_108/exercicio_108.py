import moeda

dinheiro = float(input('Digite o valor R$'))
print(f'O valor {moeda.moeda(dinheiro)} com um aumento de 10% é: {moeda.moeda(moeda.aumentar(dinheiro, 10))}')
print(f'O valor {moeda.moeda(dinheiro)} com um diminuimento de 10% é: {moeda.moeda(moeda.diminuir(dinheiro, 10))}')
print(f'O valor {moeda.moeda(dinheiro)} dobrado é: {moeda.moeda(moeda.dobro(dinheiro))}')
print(f'O valor {moeda.moeda(dinheiro)} dividido por 2 é: {moeda.moeda(moeda.metade(dinheiro))}')
 