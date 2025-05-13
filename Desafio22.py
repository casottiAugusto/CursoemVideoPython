'''
Cria um programa que lei o nome completo de uma pessoa e mostre:
-o nome com todas as letras minusculas;
-o nome com todas as letras maiusculas;
-quantos letras tem sem todo sem espaço
-quantas tetras tem o primeiro nome
'''


nome = str(input('Digite seu nome completo: ')).strip()
nomes = nome.lower()
nomes=nome.upper()
nomes=nome.split()
print('O tamanho do nome é:{}'.format(len(nome)-nome.count(' ')))
print('Tem quantos espaços:{}'.format(nome.find(' ')))
