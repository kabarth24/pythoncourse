idade18 = total_homens = total_mulheres20 = 0
while True:
  pessoa_idade = int(input('Idade: '))
  pessoa_sexo = ' '

  while pessoa_sexo not in 'MF':
    pessoa_sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
  if pessoa_idade >= 18:
    idade18 += 1
  if pessoa_sexo == 'M':
    total_homens += 1
  if pessoa_sexo == 'F' and pessoa_idade < 20:
    total_mulheres20 += 1

  
  entrada_usuario = ' '
  while entrada_usuario not in 'SN':
    entrada_usuario = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
  if entrada_usuario == 'N':
    break

print(f'Total de pessoas com mais de 18 anos: {idade18}')
print(f'Ao todo temos {total_homens} homens cadastrados')
print(f'E temos {total_mulheres20} mulheres com menos de 20 anos')