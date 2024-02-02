valores = list()
for i in range(0, 5):
  valores.append(int(input('Digite um número inteiro: ')))

print(valores)

maior_valor = max(valores)
menor_valor = min(valores)
print(f'O maior valor foi {maior_valor} e o menor valor foi {menor_valor}')

indice_maior_valor = valores.index(maior_valor)
indice_menor_valor = valores.index(menor_valor)
print(f'O maior valor foi encontrado na posição {indice_maior_valor} e o menor valor na posição {indice_menor_valor}')