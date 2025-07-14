import time
print('\033[1;37m-------- Caixa ----------\033[m')
cedula50 = cedula20 = cedula10 = cedula1 = 0

valor = int(input('Digite um valor para saque: \033[1;32mR$ '))
print('\033[m\n')
total = valor
for c in range(valor, 0, -50):
    if total >= 50:
        total = total - 50
        cedula50 = cedula50 + 1
    restante = total  
for c in range(restante, 0, -20):
    if restante >= 20:
        restante = restante - 20
        cedula20 = cedula20 + 1
    restante = restante
for c in range(restante, 0, -10):
    if restante >= 10:
        restante = restante - 10
        cedula10 = cedula10 + 1
    restante = restante
for c in range(restante, 0, -1):
    if restante >= 1:
        restante = restante - 1
        cedula1 = cedula1 + 1
    
print('\033[1;33m------ Liberando ------'.upper())
time.sleep(1)
if cedula50 > 0:    
    print(f'\033[mLiberado \033[1;27m{cedula50}\033[m cédulas de\033[1;32m R$50\033[m')
if cedula20 > 0: 
    print(f'\033[mLiberado \033[1;27m{cedula20}\033[m cédulas de\033[1;32m R$20\033[m')
if cedula10 > 0: 
    print(f'\033[mLiberado \033[1;27m{cedula10}\033[m cédulas de\033[1;32m R$10\033[m')
if cedula1 > 0: 
    print(f'\033[mLiberado \033[1;27m{cedula1}\033[m cédulas de \033[1;32mR$1\033[m')
