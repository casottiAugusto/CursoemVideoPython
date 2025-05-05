'''
Faça um programa que leia um angulo quanlque e mostra na tela o valor do seno,cosseno e tangente desse angulo
'''
import math
angulo = float(input('Informe o angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O valor do seno: {:.2f},o do cosseno: {:.2f} ,o tangente: {:.2f}'.format(seno,cosseno,tangente))