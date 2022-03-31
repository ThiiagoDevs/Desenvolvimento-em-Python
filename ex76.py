'''Crie um programa que tenha uma tupla única com nomes de produtos e
 mostre seu preços, na sequência. No final, mostre uma listagem de preços
 organizando os dados em forma tabular.'''
listagem = ('Lápis', 1.75,
            'Borracha', 0.50,
            'Caderno', 15.90,
            'Estojo', 18.50,
            'Transferidor', 6.56,
            'ComPasso', 9.98,
            'Mochila', 367.25,
            'kitcanetas', 22.55,
            'Livros', 34.99)
print('='*40)
print(f'{"MATÉRIAIS ESCOLARES":^40}')
print('='*40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('='*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>5.2f}')
print('='*40)
