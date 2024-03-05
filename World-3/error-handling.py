try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"O resultado da divisão é: {resultado}")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Erro: Você deve digitar um número inteiro.")
finally:
    print('Volte sempre!!')
