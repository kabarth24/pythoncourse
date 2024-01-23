from random import randint

print(
  '''
  Sou seu computador...
  Acabei de pensar em um número entre 0 e 10.
  Será que você consegue adivinhar qual foi?
  ''')
numero_maquina = randint(0, 10)

contagem_palpites = 0

acertou = False
while not acertou:
  numero_usuario = int(input('Qual é o seu palpite? '))
  contagem_palpites += 1

  if numero_usuario == numero_maquina:
    acertou = True
  else:
    if numero_usuario < numero_maquina:
      print('Mais... Tente mais uma vez. ')
    elif numero_usuario > numero_maquina:
      print('Menos... Tente mais uma vez. ')
    

print(f'Acertou em {contagem_palpites} tentativas. Parabéns!')
