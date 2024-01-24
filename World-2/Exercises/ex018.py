cont = soma = 0

while True:
  numero = int(input('Digite um número: '))

  if numero == 999:
    break
  cont += 1
  soma += numero

print(f'Foram digitados {cont} números e a soma deles é igual a {soma}')
