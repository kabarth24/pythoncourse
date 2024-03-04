import moedas

preco = float(input('Digite o preço: R$'))
print(f'A metade de {preco} é {moedas.metade(preco)}')
print(f'O dobro de {preco} é {moedas.dobro(preco)}')
print(f'Aumentando 10%, temos {moedas.aumentar(preco)}')
print(f'Reduzindo 10%, temos {moedas.diminuir(preco)}')
