def soma(a, b):
  return a + b

print(soma(4, 5))
print(soma(8, 9))
print(soma(2, 1))

# Podemos passar parâmetros com tamanhos variáveis utilizando o asterísco *
# Ele devolve uma tupla (imutavel)
def contador(* num):
  tamanho = len(num)
  print(f'Recebi os valores {num} e são ao todo {tamanho} números')

contador(2, 1, 7)
contador(5, 10)
contador(6, 12, 18, 24, 30)