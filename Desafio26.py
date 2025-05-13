'''
faça um programa que leia uma frase pelo telcado e mostre
-quantas vezes aparece a letra 'a'
-em que posição ela aparece a primeira vez
-em que posiçãio ela aparece a ultima vez
'''
frase=str(input('Digite uma frase: ')).upper().strip()
print('Esta frase tem {} letras A'.format(frase.count('A')))
print('A primeira letra A esta na posição {} '.format(frase.find('A')+1))
print('A ultima leta A esta na posição {}'.format(frase.rfind('A')+1))

