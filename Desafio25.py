'''
Crie um programa que leia o nome de uma pessoa e diga e ela tem silva no nome.
'''
nome = input('Digite seu nome: ').strip()
print('Seu nome tem silva {} '.format('SILVA' in nome.upper()))
