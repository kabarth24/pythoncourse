sexo = str(input('Informe o seu sexo: [M/F] ')).upper().strip()[0]

while sexo != 'M' and sexo != 'F':
  sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ').upper())

print(f'Sexo {sexo} registrado com sucesso.')
