


while True:
    print(10*'-','tabuada'.upper(),10*'-')
    num = int(input('Digite o número: '))
    if num < 0:
        break
    for c in range(1, 10 + 1):
        multiplicacao = c * num
        print(f'{num} * {c} = {multiplicacao}')
print('parou'.upper())