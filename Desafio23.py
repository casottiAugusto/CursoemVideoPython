'''
Faça um programa que leia o número de 0 a 9999 e mostre na tela a cada numero separado.
'''
numero=int(input('Informe o número'))
u=numero % 10
d=numero // 10 % 10
c=numero // 100 % 10
m=numero // 1000 % 10
print(10*'-')
print('A unidade é {}'.format(u))
print('A dezena é {}'.format(d))
print('A centena é {}'.format(c))
print('A milhar é {}'.format(m))