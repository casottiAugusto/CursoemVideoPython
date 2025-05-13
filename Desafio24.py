'''
Cri um programa que leia o nome de uma cdade e diga se ela começa ou não com o nome santo
'''
cidade = input('Em que cidade você nasceu? ').title().split()
print('Santo' in cidade[0])