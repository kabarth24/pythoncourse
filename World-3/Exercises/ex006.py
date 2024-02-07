valores = list()

while True:
  numero = int(input('Digite um número: '))

  if numero in valores:
    print('Número já cadastrado, digite outro.')
  else:
    valores.append(numero)

  confirmacao = str(input('Você quer continuar? (S/N) ')).upper().strip()
  if confirmacao == 'N':
    break

valores.sort()
print(f'Lista em ordem numérica: {valores}')
