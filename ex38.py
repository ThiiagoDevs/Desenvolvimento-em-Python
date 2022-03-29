'''Faça um programa que leia dois números inteiros e compare-os
mostrando na Tela uma mensagem:'''
n1 = int(input('Prineiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O primeiro valor é maior. ')
elif n2 > n1:
    print('O segundo número é maior. ')
else:
    print('Os dois valores sao iguais. ')
