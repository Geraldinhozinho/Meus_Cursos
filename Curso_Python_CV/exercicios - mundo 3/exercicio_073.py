import time

times = (
    "Corinthians", "Palmeiras", "Santos", "Grêmio", "Cruzeiro",
    "Flamengo", "Vasco", "Chapecoense", "Natal", "Atlético", "Botafogo-PR",
    "Bahia", "São Paulo", "Fluminense", "Sport Recife", "EC Vitória",
    "Coritiba", "Avaí", "Ponte Preta", "Atlético Goianiense"
)
cont0 = 1
cont = 1
cont1 = 0
cont2= -3
cont3= -4
cont5 = 0
print(7*'\033[1m----','CINCO PRIMEIROS CLASSIFICADOS', 7*'\033[1m----\033[m','\n')
for c in range(0, 5):
    if cont1 < 4:
        print(f'{cont}º'," ".join(times[cont1:cont]),end= '       ')
        cont = cont + 1
        cont1 = cont1 + 1
    else:
        print(f'{cont}º'," ".join(times[cont1:cont]))
        
print(7*'\033[1m----','CINCO ÚLTIMOS CLASSIFICADOS', 7*'\033[1m----\033[m','\n')
for c in range(0, 3):
    print(f'{cont0}º',' '.join(times[cont3:cont2]),end= '       ')
    cont2 = cont2 + 1
    cont3 = cont3 + 1
    cont0 = cont0 +1
    if cont2 == 0:
        print(f'{cont0}º',times[-1])
        
print(7*'\033[1m----','TIMES EM ORDEM ALFABÉTICA', 7*'\033[1m----\033[m','\n')
sorted = sorted(times)
for c in sorted:
    if cont5 < 4:
        print(c, end=' ->    ', flush= True)
        time.sleep(0.8)
        cont5 = cont5 +1
    else:
        print(c, flush= True)
        cont5 = 0
    if cont5 % 5 == 0:
        print('')
        cont5 = 0
print(7*'\033[1m----','O TIME DA CHAPECOENSE APARECE NA:', 7*'\033[1m----\033[m','\n')
print(26*' ','----------->',times.index('Chapecoense'), 'ª POSIÇÃO', ' <-----------')
    
# lista = ('a','b','c','d','e','f')
# # print(lista)
# # print(lista[0])
# # print(lista[-1])

# # for cont in lista:
# #     print(cont)
# #     print(lista)


# # for cont in range(2, len(lista)):
# #     print(len(lista))


# for pos, cont in enumerate(lista):
#     print(lista)