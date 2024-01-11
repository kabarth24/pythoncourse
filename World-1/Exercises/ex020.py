frase = str(input('Digite uma frase: ')).strip().upper()

quantidade_letra_a = frase.count('A')
primeira_posicao = frase.find('A') + 1
ultima_posicao = frase.rfind('A') + 1

print(f'A letra "A" aparece {quantidade_letra_a} vezes')
print(f'A letra "A" aparece pela primeira vez na posição {primeira_posicao}')
print(f'A letra "A" aparece pela última vez na posição {ultima_posicao}')
