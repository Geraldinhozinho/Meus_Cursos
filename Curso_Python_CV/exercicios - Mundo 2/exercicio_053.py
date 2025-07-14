
frase = str(input('DIGITE UMA FRASE: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]
print(junto,' / ',inverso)
if junto == inverso:
    print('PALÍNDROMO')
else:
    print('NÃO É PALÍNDROMO')