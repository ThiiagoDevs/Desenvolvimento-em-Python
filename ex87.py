'''Exercício 87 – Mais sobre Matriz em Python'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = maior = scol = 0
for L in range(0, 3):
    for c in range(0, 3):
        matriz[L][c] = int(input(f'Digite um valor para [{L}, {c}]: '))
print('-=' * 30)
for L in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[L][c]:^5}]', end='')
        if matriz[L][c] % 2 == 0:
            spar += matriz[L][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar} ')
for L in range(0, 3):
    scol += matriz[L][2]
print(f'A soma dos valores da terceira coluna é {scol} ')
for L in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior} ')
print('-=' * 30)
