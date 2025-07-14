numero = int(input('Digite um número: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(' \033[1;32mUnidade: {:1}\n \033[1;33mDezena: {:2}\n \033[1;34mCentena: {:1}\n \033[1;35mMilhar: {:2}\033[m'.format(u,d, c, m))