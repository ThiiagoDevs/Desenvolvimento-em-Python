'''Analizando dados em uma Tupla'''
núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite ultimo número: ')))
print(f'Você digitou os valores {núm}')
print(f'O valor 5 apareceu {núm.count(5)} vezes')
if 9 in núm:
    print(f'O valor 9 apareceu na {núm.index(9)+1}° posição')
else:
    print('O valor 9 nao foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')
