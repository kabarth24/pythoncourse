import random

numero_aleatorio = random.randint(0, 5)

numero_usuario = int(input('Digite um número inteiro entre 0 e 5: '))

if numero_usuario == numero_aleatorio:
  print('Você acertou! PARABÉNS!')
else:
  print('O computador venceu! TENTE NOVAMENTE!')
