from moeda import moeda
from dados import dado


p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 80, 30) 