def área(larg, comp):
    á = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {á}m²')


# programa principal
print('  Controle de terrenos')
print('-' * 30)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
área(larg, comp)
