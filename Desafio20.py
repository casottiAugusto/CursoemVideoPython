'''
Faça um programa para sortear a orde de apresetação do trabalho de escola
'''
from random import shuffle

n1=input('Informe o terceiro nome: ')
n2=input('Informe o quarto nome: ')
n3=input('Informe o terceiro nome: ')
n4=input('Informe o quarto nome: ')
lista = [n1,n2,n3,n4]
shuffle(lista)
print('A orden sera: {}'.format(lista))


