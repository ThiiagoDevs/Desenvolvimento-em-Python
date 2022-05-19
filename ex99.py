from time import sleep


def maior(* núm):
    cont = maior = 0
    print('-=' * 40)
    print('Analizando os valores passados... ')
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.4)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} ao todo.')
    print(f' O maior valor informado foi {maior}')


# programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6,)
maior()
