'''
Um professor que sortear um do seus quatros alunos pára apagar o quadro.faço um programa que ajude ele
lendo o nome deles e escrevendo o nome do escolhido

'''
from random import choice

n1=input('Informe o primeito nome: ')
n2=input('Informe o segundo nome: ')
n3=input('Informe o terceiro nome: ')
n4=input('Informe o quarto nome: ')
lista = [n1,n2,n3,n4]
escolhido = choice(lista)
print('O escolhido foi {}'.format(escolhido))