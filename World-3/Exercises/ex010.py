from random import randint
from time import sleep

jogadores = dict()

for i in range(1, 5):
    jogadores[f'Jogador {i}'] = randint(1, 6)

for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(0.5)

# jogadores_ordenados = dict(sorted(jogadores.items(), key = lambda item : item[1]))

for i, (k, v) in enumerate(sorted(jogadores.items(), key=lambda item: item[1], reverse=True), 1):
    print(f'{i}º lugar: {k} com {v}')
    sleep(0.5)
