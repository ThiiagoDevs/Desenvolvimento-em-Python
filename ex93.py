'''Exercício 93 – Cadastro de Jogador de Futebol'''
jogador = dict()
jogos = list()
jogador['nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partida {jogador["nome"]} jogou? '))
for c in range(0, total):
    jogos.append(int(input(f'Quantos gols fez no jogos {c}? ')))
jogador['gols'] = jogos[:]
jogador['total'] = sum(jogos)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'Jogador {jogador["nome"]} jogou {len(jogador["gols"])} jogos.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols. ')
print(f'  Foi um total de {jogador["total"]} gols.')
