
valor = int(input('Digite um valor: '))
fat = 1

print('{}! = '.format(valor), end='')

for c in range(valor, 0, -1):
    fat *= c
    if c > 1:
        print(c, end=' x ')
    else:
        print(c, end=' = ')

print(fat)



# n = int(input('Digite o numero. '))
# c = n
# f = 1
# print('Calculando fatorial {}! = '.format(n), end='')
# while c > 0:
#     if c > 1:
#         print(c, end=' x ')
#     else:
#         print(c, end=' = ')
#     f *= c
#     c -= 1
# print('\33[1;7m {} \33[m '.format(f))



