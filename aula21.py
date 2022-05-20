'''def contador(i, f, p):
    """_summary_

    Args:
        i (_para _): _inicializa a contagem e mosta na tela _
        f (_para_): _mostra o fim da contagem na tela_
        p (_para _): _proceso da contagem na tela_
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('Fim')


help(contador)'''

# parametro opcional


'''def soma(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


soma(a=5, c=9)
soma(8, 4)
soma()'''


'''def função():
    n1 = 5
    print(f'n1 dentro vale {n1}')


n1 = 2
função()
print(f'n1 fora vale {n1}')'''


'''def soma(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = soma(3, 2, 5)
r2 = soma(8, 4)
r3 = soma(3)
print(f'Meus cálculos deram {r1}, {r2}, e {r3}.')'''


def fatorial(núm=1):
    f = 1
    for c in range(núm, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
