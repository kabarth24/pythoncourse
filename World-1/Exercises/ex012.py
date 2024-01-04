salario_atual = float(input('Digite o seu salário atual: '))

aumento_salario = salario_atual * 0.15
salario_novo = salario_atual + aumento_salario

print(f'O novo salário deste funcionário é R${salario_novo:.2f}')
