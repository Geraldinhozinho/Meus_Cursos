soma = contador = 0

while True:
    num = int(input('Digite números: [999 para parar]'))
    if num == 999:
        break
    soma = soma + num
    contador = contador + 1
print(f'A soma de todos os números é {soma}, e foram digitados {contador} números')