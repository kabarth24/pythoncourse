from datetime import date

data_atual = date.today().year

contador_menor_idade = 0
contador_maior_idade = 0
for i in range(1, 8):
  ano_de_nascimento = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
  if data_atual - ano_de_nascimento < 18:
    contador_menor_idade += 1
  else:
    contador_maior_idade += 1

print(f'Ao todo tivemos {contador_menor_idade} pessoas menores de idade')
print(f'E também tivemos {contador_maior_idade} pessoas maiores de idade')
