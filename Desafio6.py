#faça um  script que leia o numero  e mostre seu dobro triplo e rais quadrada
import math
a=int(input('Informe o número que você quer:'))

print('O número informado é {} seu dobro é {} ,o triplo é {},a raiz quadrada é {:.2f}'.format(a,(a*2),(a*3),math.sqrt(a)))