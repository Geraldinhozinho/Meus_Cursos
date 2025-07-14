

Palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')


cont = 1

for tudo in Palavras:
    print(f'\nNa palavra {tudo.upper()} temos ', end= '')
    for letras in tudo:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')