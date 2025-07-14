soma = contador = quantidade = maior = menor = a = 0
termos = 1
mais = 'S'
while mais != 'N':
    quantidade = quantidade + 2
    while contador < quantidade :
        num = int(input('Digite {}º valor: '.format(termos)))
        if contador == 0:
            maior = num
            menor = num
        else:
            if num > maior:
                maior = num
            elif num < menor:
                menor = num
        soma = soma + num
        contador = contador + 1
        termos = termos +1
    mais = str(input('deseja mostrar mais números? s / n: ').upper())
    while mais != 'S' and mais != 'N':
        print('inválido, repita')
        mais = str(input('deseja mostrar mais números? s / n: ').upper())

# Exibe os resultados finais
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')
print(f'A soma dos valores é {soma}')
print(f'A média dos valores é {soma/contador}')
print(f'Foram digitados {contador} números.')
