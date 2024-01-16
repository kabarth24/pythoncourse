print('=========== LOJAS BARTH ===========')

preco_produto = float(input('Preço das compras: R$'))

print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')

opcao_usuario = int(input('Qual a opção? [1 a 4]: '))

if opcao_usuario == 1:
    preco_produto_desconto = preco_produto - (preco_produto * 0.10)
    print(
        f'Sua compra de R${preco_produto:.2f} vai custar R${preco_produto_desconto:.2f} no final.')
elif opcao_usuario == 2:
    preco_produto_desconto = preco_produto - (preco_produto * 0.05)
    print(
        f'Sua compra de R${preco_produto:.2f} vai custar R${preco_produto_desconto:.2f} no final.')
elif opcao_usuario == 3:
    print(f'Sua compra no final ficou R${preco_produto:.2f} em 2x no cartão.')
elif opcao_usuario == 4:
    preco_produto_juros = preco_produto + (preco_produto * 0.20)
    parcela = int(input('Quantas parcelas? '))
    valor_parcela = preco_produto / parcela
    print(
        f'Sua compra de R${preco_produto:.2f} ficou em {parcela}x de R${valor_parcela:.2f}. Vai custar R${preco_produto_juros:.2f} no final.')
else:
    print('Opção inválida! Insira um número de 1 a 4 para prosseguir com a sua compra.')