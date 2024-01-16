peso = float(input('Insira o seu peso (Kg): '))
altura = float(input('Insira a sua altura (m): '))

imc = peso / (altura * altura)

abaixo_do_peso = 18.5
peso_ideal = 25
sobrepeso = 30
obesidade = 40

if imc <= abaixo_do_peso:
    print(f'O seu IMC é de {imc:.2f}, você está ABAIXO DO PESO!')
elif imc <= peso_ideal:
    print(f'O seu IMC é de {imc:.2f}, você está em seu PESO IDEAL!')
elif imc <= sobrepeso:
    print(f'O seu IMC é de {imc:.2f}, você está em SOBREPESO!')
elif imc <= obesidade:
    print(f'O seu IMC é de {imc:.2f}, você está com OBESIDADE!')
else:
    print(f'O seu IMC é de {imc:.2f}, você está com OBESIDADE MORBIDA!')
