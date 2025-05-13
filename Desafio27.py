'''
Faça um programa que leia o nome de uma pessoa,e mostre  o primeiro e o ultimo nome de uma pessoa separadamente
'''
nome=str(input('Digite seu nome: ')).strip().upper()
print('Seu primeiro nome é {}'.format(nome.split()[0]))
print('Seu Ultimo nome é {}'.format(nome.split()[-1]))
