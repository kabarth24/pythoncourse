from time import sleep
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''
Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogada_usuario = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('=-' * 15)
print(f'O jogador escolheu {(itens[jogada_usuario])}')
print(f'O computador escolheu {(itens[computador])}')
print('=-' * 15)

if computador == 0:
    if jogada_usuario == 0:
        print('JOGADA DEU EMPATE!')
    elif jogada_usuario == 1:
        print('JOGADOR VENCE!')
    elif jogada_usuario == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('Jogada inválida!')

elif computador == 1:
    if jogada_usuario == 0:
        print('COMPUTADOR VENCE!')
    elif jogada_usuario == 1:
        print('JOGADA DEU EMPATE!')
    elif jogada_usuario == 2:
        print('JOGADOR VENCE!')
    else:
        print('Jogada inválida!')

elif computador == 2:
    if jogada_usuario == 0:
        print('JOGADOR VENCE!')
    elif jogada_usuario == 1:
        print('COMPUTADOR VENCE!')
    elif jogada_usuario == 2:
        print('JOGADA DEU EMPATE!')
    else:
        print('Jogada inválida!')