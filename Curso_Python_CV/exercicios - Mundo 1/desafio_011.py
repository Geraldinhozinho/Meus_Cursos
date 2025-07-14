print('======Desafio 10 ======')


Altura = float(input('\033[1;32;40mQual a altura da parede: \033[m'))
Largura = float(input('\033[1;44mQual a largura da parede: \033[m'))

Area = Altura * Largura
Tinta = Area / 2

print('\033[1mA área da parede é {} M²\033[1;31m\nÉ preciso {} Litros de tinta para pintar essa parede.\033[m'.format(Area, Tinta))