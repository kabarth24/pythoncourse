from datetime import date

data_de_nascimento = int(input('Digite o ano que você nasceu: '))
ano_atual = date.today().year

idade = ano_atual - data_de_nascimento
ainda_vai_se_alistar = 18 - idade
ano_de_alistamento = data_de_nascimento + 18

if idade < 18:
  print(f'Você tem {idade} anos. Faltam {ainda_vai_se_alistar} anos para você se alistar!')
  print(f'Seu alistamento será em {ano_de_alistamento}')
elif idade == 18:
  print(f'Você tem {idade} anos. Está na hora de se alistar!')
else:
  print(f'Você tem {idade} anos. Seu ano de alistamento foi em {ano_de_alistamento}!')
