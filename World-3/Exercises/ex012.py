dados_pessoais = dict()
dados_pessoais_lista = list()
soma = media = 0

while True:
  dados_pessoais.clear()
  dados_pessoais['Nome'] = str(input('Nome: '))

  while True:
    dados_pessoais['Sexo'] = str(input('Sexo: ')).upper()[0]
    if dados_pessoais['Sexo'] in 'MF':
      break
    print('Erro! Digite apenas M ou F.')

  dados_pessoais['Idade'] = int(input('Idade: '))
  soma += dados_pessoais['Idade']

  dados_pessoais_lista.append(dados_pessoais.copy()) 

  while True:
    confirmacao = str(input('Quer continuar? [S/N] ')).upper()[0]
    if confirmacao in 'SN':
      break
    print('ERRO! Responda apenas S ou N.')
  if confirmacao == 'N':
    break

media = soma / len(dados_pessoais_lista)

print(f'A) Ao todo temos {len(dados_pessoais_lista)} pessoas cadastradas')
print(f'B) A média de idade é de {media:5.2f} anos')
print('C) As mulheres cadastradas foram ', end='')
for p in dados_pessoais_lista:
  if p['Sexo'] == 'F':
    print(f'{p["Nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ', end='')
for p in dados_pessoais_lista:
  if p['Idade'] >= media:
    print(f'{p['Nome']} com {p['Idade']} anos | ', end='')
