numeros_por_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
  numero_do_usuario = int(input('Digite um número entre 0 e 20: '))
  
  if 0 <= numero_do_usuario <= 20:
    break
  print('Tente novamente. ', end='')

numero = numeros_por_extenso[numero_do_usuario]

print(f'Você digitou o número {numero}')
