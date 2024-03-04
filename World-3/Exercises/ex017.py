def ficha(nome = "Não identificado", gols = 0):
  """""""""
  Esta função retorna o nome do jogador e a quantidade de gols feito pelo mesmo.
  :param nome: Nome do jogador, caso não informado, retornará como "Não identificado"
  :param gols: Quantidade de gols feito pelo jogador, caso não informado, retornará como "Quantidade de gols não informado"
  """""""""
  print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

nome_jogador = str(input('Nome do jogador: '))
quantidade_gols = str(input('Número de gols: '))

if quantidade_gols.isnumeric():
  quantidade_gols = int(quantidade_gols)
else:
  quantidade_gols = 0
if nome_jogador.strip() == '':
  ficha(gols = quantidade_gols)
else:
  ficha(nome_jogador, quantidade_gols)
  