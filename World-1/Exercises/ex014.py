from random import choice

primeiro_aluno = str(input('Digite o nome do primeiro aluno: '))
segundo_aluno = str(input('Digite o nome do segundo aluno: '))
terceiro_aluno = str(input('Digite o nome do terceiro aluno: '))
quarto_aluno = str(input('Digite o nome do quarto aluno: '))

sorteio_apagar_quadro = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]

nome = choice(sorteio_apagar_quadro)

print(f'O aluno sorteado para apagar o quadro foi o {nome}')
