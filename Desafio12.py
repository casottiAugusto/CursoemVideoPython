#faça um algoritomo que leia o preço de um produto e mostre o acressimo de 15 %
import math
preco=float(input('Infome o proço do produto '))
acres=preco*0.15
print('O produto no peço {},mas com acessimo de %15 e de {:.2f}.'.format(preco,(acres+preco)))