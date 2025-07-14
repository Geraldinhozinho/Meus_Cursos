import datetime
anoatual = datetime.date.today().year
dic = {}
nome = str(input('Digite seu nome: '))
dic ['Nome'] = nome

ano = int(input(f"Digite seu ano de nascimento {dic['Nome']}: "))
dic['Idade'] = anoatual - ano

resp = int(input(f"Carteira de Trabalho {dic['Nome']}: (0 para não tem) "))

if resp != 0:
    ano_cont = int(input(f"Digite o ano de contratação {dic['Nome']}: "))
    dic['Ano_cont'] = ano_cont
    salario = int(input(f"Digite seu salário {dic['Nome']}: "))
    dic['Salario'] = salario
    dic['Aposentadoria'] = 60 - (anoatual - ano_cont)  
print(30*'=')
for k, v in dic.items():
    print(f'{k} tem o valor {v}')


