print('===== desafio 73 ====='.upper())

times = ('Athletico-PR', 'Internacional', 'Atletico-MG', 
            'Gremio', 'Atletico-GO', 'Vasco', 'Bahia', 
            'Sao Paulo', 'Sport-Recife', 'Flamengo', 'Palmeiras', 
            'Bragantino', 'Botafogo', 'Ceara', 'Corinthians', 
            'Goias', 'Fluminense', 'Santos', 'Fortaleza', 'Coritiba')
print('-='*50)
print(f'Lista dos 20 colocados do CAMPEONATO BRASILEIRO: {times}')


print('-='*50)
print(f'Os 5  primeiros colcados: {times[0:5]}')

print('-='*50)
print(f'Os 4 ultimos colocados: {times[-4:]}')

print('-='*50)
print(f'Times em ordem alfabetica: {sorted(times)}')

print('-='*50)
print(f'Chapecoense esta na {times.index("Chapecoense")+1}ª posição')
print('-='*50)