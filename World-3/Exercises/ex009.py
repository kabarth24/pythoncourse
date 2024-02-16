situacao = dict()

situacao['nome'] = str(input('Nome: '))
situacao['media'] = float(input(f'Média de {situacao["nome"]}: '))

if situacao['media'] >= 7:
  situacao['situacao'] = 'Aprovado'
elif 5 <= situacao['media'] < 7:
  situacao['situacao'] = 'Recuperação'
else:
  situacao['situacao'] = 'Reprovado'

for k, v in situacao.items():
  print(f' - {k} é igual a {v}')