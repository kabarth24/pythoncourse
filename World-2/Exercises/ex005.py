from datetime import date

ano_de_nascimento = int(input('Digite o seu ano de nascimento: '))
ano_atual = date.today().year
idade_atleta = ano_atual - ano_de_nascimento

atleta_mirim = 9
atleta_infantil = 14
atleta_junior = 19
atleta_senior = 25

if idade_atleta <= atleta_mirim:
  print(f'O atleta tem {idade_atleta} anos')
  print(f'Classificação: MIRIM')
elif idade_atleta <= atleta_infantil:
  print(f'O atleta tem {idade_atleta} anos')
  print(f'Classificação: INFANTIL')
elif idade_atleta <= atleta_junior:
  print(f'O atleta tem {idade_atleta} anos')
  print(f'Classificação: JUNIOR')
elif idade_atleta <= atleta_senior:
  print(f'O atleta tem {idade_atleta} anos')
  print(f'Classificação: SENIOR')
else:
  print(f'O atleta tem {idade_atleta} anos')
  print(f'Classificação: MASTER')
