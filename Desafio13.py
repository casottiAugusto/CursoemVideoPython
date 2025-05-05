'''
faça um açgortomo que leia o salario de um colaborador e moste seu novo salarao,
com 15% de aumento
'''

n=float(input('Infome o novo salario: '))
ajuste=n+(n*15/100)
print('O valor a do salario atual é: {:.2f}'.format(ajuste))
