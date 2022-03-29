times = ('Sao paulo', 'Palmeiras', 'Santos', 'Gremio',
         'Cruzeiro', 'Corinthians', 'flamengo', 'Vasco',
         'Chapecoense', 'Atletico', 'Bahia', 'Sporte Recife',
         'Atletico-PR', 'Fluminense', 'EC vitoria', 'coritiba', 'avai',
         'Ponte Preta', 'Atletico-GO')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os cincos primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os quatros ultimos times são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=' * 15)
print(f'O Cruzeiro está na {times.index("Cruzeiro")+1}° posição')
