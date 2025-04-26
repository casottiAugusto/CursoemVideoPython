#crie um programa que leia a quantidade de grana e mostre a quantidade de dolar que pode cmprar
#Levando em consideração o U$1,00 =R3,27
r=float(input('Informe a quantidade de dinheiro na carteira:R$'))
conv=r*3.27
print('O dinheiro que vc tem e de {} que da para conprar UR${} en dolar '.format(r,conv))