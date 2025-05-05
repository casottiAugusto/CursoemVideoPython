'''
Faça um programa que leia o comprimeto do cateto oposto e do cateto
adjacemte de , trianguo retangulo,calcule e mostre o comprimento
da hipotenusa
'''
import math
co=float(input('Informe o cateto oposto: '))
ca=float(input('Informe o cateto adjacente: '))
hi=math.hypot(co,ca)
print('O valor da hipotenusa é: {:.2f}'.format(hi))
