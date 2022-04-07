'''Dividindo valores em várias listas'''
núm = list()
pares = list()
impares = list()
while True:
    núm.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(núm):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('=' * 30)
print(f'A lista completa e {núm} ')
print(f'A lista de pares é {pares} ')
print(f'A lista de impares é {impares} ')
