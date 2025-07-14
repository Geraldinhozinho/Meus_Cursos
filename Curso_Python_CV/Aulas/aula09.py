# frase =  '             Alana linda vai casar comigo             '

# print('FATIAMENTO')
# print(frase[2])
# print(frase[0:6])
# print(frase[0:6:2])
# print(frase[:10:2])
# print(frase.find('n'))
# print('\n')

# print('Análise')
# print(len(frase))
# print(frase.count('a'))
# print(frase.count('a',0,6))
# print(frase.find('n'))
# print(frase.find('z'))
# print('A' in frase)
# print('\n')

# print('TRANSFORMAÇÃO')
# print(frase.replace('ana', 'gaio'))
# print(frase.upper())
# print(frase.lower())
# print(frase.capitalize())
# print(frase.title())
# print(frase.format())
# print(frase.strip())
# print(frase.rstrip())
# print(frase.lstrip())
# print(frase.split())
# recebe =frase.split()
# print( len(recebe[0]), recebe[1])



# print('')
# print(frase.count('a',0,6))

# print(frase.split())
# print(frase.strip())

# print('a')
# print(frase.lstrip())




frase =  '             Alana linda vai casar comigo             '
print('------------Fatiamento-----------')

print('------------Análise-----------')
print(len(frase))
print(frase.count('a'))
print(frase.count('a',0,12))
print(frase.find('ana')) #encontrou o ana na frase e qual posição, apareceu na posição tal
print('Alana' in frase)

print('------------Transformação-----------')
print(frase.replace('Alana', 'Papagaio'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())#retira os espaços das extremidades, há a variação right e left
print(frase.rstrip())
print(frase.lstrip())

print('------------Divisão-----------')
print(frase.split())

print('------------Junção-----------')

print('-'.join(frase))







