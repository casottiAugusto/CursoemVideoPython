#faça um programa que leia a altura e largura da parede ,ecalcule a area,e calcule
#a quantidade de tinta para pintala ,lebrando que um balde de tinta pinta uma area de 2m²
comp=float(input('Informe e altura: '))
lag=float(input('Informe e largura: '))
area=comp*lag
print('A Aréa total é de :{}m²'.format(area))
print('Para pintar tudo sera necessario {} latas  tinta'.format(int(area/2)))
