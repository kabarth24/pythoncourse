numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))

if numero1 > numero2:
  print('O PRIMEIRO número É MAIOR')
elif numero2 > numero1:
  print('O SEGUNDO número É MAIOR')
else:
  print(f'Não existe valor maior, o número {numero1} e {numero2} são iguais')
