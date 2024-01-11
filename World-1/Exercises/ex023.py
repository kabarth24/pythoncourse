velocidade_do_carro = float(input('Qual foi a velocidade do carro? '))

limite_velocidade = 80
multa_por_km = 7

if velocidade_do_carro > limite_velocidade:
  velocidade_acima_do_limite = velocidade_do_carro - limite_velocidade
  valor_da_multa = velocidade_acima_do_limite * multa_por_km
  print(f'Você foi multado! O valor da multa é {valor_da_multa:.2f} reais')
