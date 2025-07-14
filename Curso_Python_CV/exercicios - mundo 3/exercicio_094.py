dicionario = {}
lista = []
idades = 0
while True:
    nome = str(input('Digite o nome da pessoa: '))
    dicionario['Pessoa'] = nome
    
    sexo = ''
    while sexo not in ('M', 'F'):
        sexo = input('Digite o sexo da pessoa: [M/F] ').strip().upper()
        dicionario[f'Sexo'] = sexo
        if sexo != 'M' and sexo != 'F':
            print('tente novamente... apenas [M ou F]'.upper(),end=' => ')
            
    idade = int(input('Digite a idade da pessoa: '))
    dicionario[f'Idade'] = idade
    idades = idades + idade
    
    lista.append(dicionario.copy())
    
    continua = ' '
    while continua not in ('S', 'N'):
        continua = str(input('Deseja continuar: [S / N] ')).strip().upper()
        if continua != 'S' and continua != 'N':
            print('Tente novamente... Apenas [S ou N]'.upper(),end=' ')
    if continua == 'N':
        break
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas')
print('-='*30)

print(f'B) A média de idade é de {idades/len(lista):.2f} anos')
print('-='*30)

for cont in range(len(lista)):
    if lista[cont]['Sexo'] == 'F':
        print(f'C) Temos de mulheres: {lista[cont]["Pessoa"]}')

print('-='*30)
        
print('D) As pessoas que estão acima da média de idade são:')
for pessoa in lista:
    if pessoa['Idade'] >= idades / len(lista):
        print(f'  Nome: {pessoa["Pessoa"]:<10}  Idade: {pessoa["Idade"]} Sexo: {pessoa["Sexo"]}')

        















# dicionario = {}
# lista = []
# idades = 0

# while True:
#     nome = input('Digite o nome da pessoa: ')
#     dicionario['Pessoa'] = nome

#     sexo = ''
#     while sexo not in ('M', 'F'):
#         sexo = input('Digite o sexo da pessoa: [M/F] ').strip().upper()
#         if sexo not in ('M', 'F'):
#             print('Tente novamente... Apenas [M ou F] => ', end='')
#     dicionario['Sexo'] = sexo

#     idade = int(input('Digite a idade da pessoa: '))
#     dicionario['Idade'] = idade
#     idades += idade

#     lista.append(dicionario.copy())  # <- AQUI é essencial copiar

#     continua = ''
#     while continua not in ('S', 'N'):
#         continua = input('Deseja continuar: [S/N] ').strip().upper()
#         if continua not in ('S', 'N'):
#             print('Tente novamente... Apenas [S ou N] ', end='')

#     if continua == 'N':
#         break

# print(f'\nA) Ao todo temos {len(lista)} pessoas cadastradas')
# print(f'B) A média de idade é de {idades / len(lista):.2f} anos')

# print(f'C) Mulheres cadastradas:')
# for pessoa in lista:
#     if pessoa['Sexo'] == 'F':
#         print(f'   - {pessoa["Pessoa"]}')

# print(f'D) Pessoas acima da média de idade:')
# for pessoa in lista:
#     if pessoa['Idade'] >= idades / len(lista):
#         print(f'   {pessoa}')
