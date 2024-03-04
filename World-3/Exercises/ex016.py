def voto(ano_de_nascimento):
  """""""""
  Essa função retorna se o voto da pessoa é NEGADO, OPCIONAL ou OBRIGATÓRIO
  :param ano_de_nascimento: ano de nascimento da pessoa
  """""""""
  from datetime import datetime

  data_atual = datetime.now()
  ano_atual = data_atual.year
  idade = ano_atual - ano_de_nascimento

  if idade < 16:
    return f'Com {idade} anos, O seu voto é NEGADO.'
  elif idade <= 18 or idade >= 65:
    return f'Com {idade} anos, o seu voto é OPCIONAL.'
  else:
    return f'Com {idade} anos, o seu voto é OBRIGATÓRIO'
  
print(voto(int(input('Digite o seu ano de nascimento: '))))