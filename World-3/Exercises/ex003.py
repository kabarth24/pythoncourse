from random import randint

tupla_numeros_aleatorios = tuple(randint(1, 100) for _ in range(5))

print(tupla_numeros_aleatorios)

maior_valor = max(tupla_numeros_aleatorios)
menor_valor = min(tupla_numeros_aleatorios)

print(f'O maior valor sorteado foi {maior_valor}')
print(f'O menor valor sorteado foi {menor_valor}')
