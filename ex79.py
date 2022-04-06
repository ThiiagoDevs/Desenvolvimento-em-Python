números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso... ')
    else:
        print('Valor duplicado! nao vou adicionar...')
    r = str(input('Quer continuar [S/N]'))
    if r in 'Nn':
        break
print('-=' * 30)
números.sort()
print(f'você digitou os valores {números}')
