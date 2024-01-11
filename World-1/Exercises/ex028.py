salario = float(input('Qual é o seu salário? '))

if salario > 1250:
    porcentagem = 0.10
    novo_salario = (salario * porcentagem) + salario
    print(f'O seu salário agora é de R${novo_salario}')
else:
    porcentagem = 0.15
    novo_salario = (salario * porcentagem) + salario
    print(f'O seu salário agora é de R${novo_salario}')