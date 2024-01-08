from random import shuffle

primeiro_aluno = str(input('Digite o nome do primeiro aluno: '))
segundo_aluno = str(input('Digite o nome do segundo aluno: '))
terceiro_aluno = str(input('Digite o nome do terceiro aluno: '))
quarto_aluno = str(input('Digite o nome do quarto aluno: '))

lista_nomes = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]

shuffle(lista_nomes)

print(f'A ordem de apresentação dos trabalhos será: {lista_nomes}')
