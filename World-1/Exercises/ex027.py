numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))
numero3 = int(input('Digite um número: '))

# Menor
menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2

if numero3 < numero1 and numero3 < numero2:
    menor = numero3


# Maior
maior = numero1
if numero2 > numero1 and numero2 > numero3:
    maior = numero2

if numero3 > numero1 and numero3 > numero2:
    maior = numero3

print(f'O maior número é o {maior}')
print(f'O menor número é o {menor}')