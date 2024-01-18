soma = 0
contador = 0

for i in range(1, 7):
  numero = int(input('Digite um valor: '))
  if numero % 2 == 0:
    soma += numero
    contador += 1

print(f'Você informou {contador} numeros PARES e a soma foi {soma}')
