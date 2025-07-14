dic = {}
nome = str(input('Digite seu nome: '))
dic ['Nome'] = nome
media = float(input(f"Digite sua média {dic['Nome']}: "))
dic['Media'] = media
if dic['Media']>6.0:
    dic['Situacao'] = 'Aprovado'
else:
    dic['Situacao'] = 'Reprovado'

for k, v in dic.items():
    print(f'{k} é igual a {v}')


