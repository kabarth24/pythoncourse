valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos_para_quitar = int(input('Em quantos anos você pretende pagar? '))

prestacao = valor_casa / (anos_para_quitar * 12)
limite_prestacao = salario * 0.30

if prestacao > limite_prestacao:
  print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos_para_quitar} anos a prestação será de R${prestacao:.2f}. Empréstimo NEGADO, pois o valor da prestação excede 30% da sua renda mensal!')
else:
  print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos_para_quitar} anos a prestação será de R${prestacao:.2f}. Empréstimo APROVADO!!')
