numero = int(input('Digite um número: '))

contador = 0

for i in range(1, numero + 1):
  print(i, end= ' ')
  if numero % i == 0:
    contador += 1

if contador == 2:
  print(f'O número {numero} foi divisível {contador} vezes, sendo assim, ele é PRIMO!')
else:
  print(f'O número {numero} foi divisível {contador} vezes, sendo assim, ele NÃO é PRIMO!')