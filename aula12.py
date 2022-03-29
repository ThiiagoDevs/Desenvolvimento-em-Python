nome = str(input('Qual é o seu nome:'))
if nome == 'thiago':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular.')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome feminino.,')
else:
    print('Seu nome é bem normal. ')
print(f'Tenha um bom dia, {nome}!')
