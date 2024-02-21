from datetime import datetime

data_atual = datetime.now()
ano_atual = data_atual.year

dados_do_contribuinte = dict()

while True:
  dados_do_contribuinte['Nome'] = str(input('Nome: '))
  dados_do_contribuinte['Idade'] = ano_atual - int(input('Ano de nascimento: '))
  dados_do_contribuinte['CTPS'] = int(input('Carteira de trabalho: '))

  if dados_do_contribuinte['CTPS'] == 0:
    for k, v in dados_do_contribuinte.items():
      print(f'- {k} tem o valor {v}')
    break
  else:
    dados_do_contribuinte['Ano de contratação'] = int(input('Ano de contratação: '))
    dados_do_contribuinte['Salário'] = float(input('Salário: '))
    dados_do_contribuinte['Aposentadoria'] = (dados_do_contribuinte['Ano de contratação'] + 35) - 2000
    for k, v in dados_do_contribuinte.items():
      print(f'- {k} tem o valor {v}')
    break