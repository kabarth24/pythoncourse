while True:
  print('-' * 30)
  numero = int(input('Quer ver a tabuada de qual valor? '))

  if numero < 0:
    print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
    break
  
  for i in range(0, 11):
    multiplicacao = numero * i
    print(f'{numero} x {i} = {multiplicacao}')