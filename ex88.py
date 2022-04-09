'''Palpites para a Mega Sena'''
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-=' * 30)
print('                  JOGA NA MEGA SENA              ')
print('-=' * 30)
quant = int(input('Quantos jogos você quer que sorteie ? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        núm = randint(1, 60)
        if núm not in lista:
            lista.append(núm)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 10, f'SORTEANDO {quant} ', '-=' * 10)
for i, l in enumerate(jogos):
    print(f'jogos {i+1}: {l} ')
    sleep(1)
print('-=' * 9, '< BOA SORTE >', '-=' * 9)
