'''Exercício 93 – Cadastro de Jogador de Futebol'''
time = list()
jogador = dict()
jogos = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogos.clear()
    for c in range(0, total):
        jogos.append(int(input(f'Quantos gols fez no jogos {c+1}? ')))
    jogador['gols'] = jogos[:]
    jogador['total'] = sum(jogos)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quar continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar.) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com esse codigo {busca}! ')
    else:
        print(f' -- LAVATAMENTO DE JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'  No jogo {i+1} fez {g} gols. ')
    print('-=' * 40)
print(' <<< VOLTE SEMPRE >>>')
