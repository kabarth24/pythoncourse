lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')

# mode 1
for comida in lanche:
  print(f'Eu vou comer {comida}')

# mode 2
for cont in range(0, len(lanche)):
  print(f'Eu vou comer {lanche[cont]}')

for pos, comida in enumerate(lanche):
  print(f'Eu vou comer {comida} na posição {pos}')
