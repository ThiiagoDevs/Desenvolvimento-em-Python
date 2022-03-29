'''Faça um programa que mostre na tela uma contagem
 regressiva para o estouro de fogos de artifício'''
from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.7)
print('BUM! BUM! POOW! POOW!')
print('FELIZ 2022!')
