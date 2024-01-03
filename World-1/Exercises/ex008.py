nome_aluno = input('Digite o nome do aluno: ')

nota1 = int(input(f'Digite a primeira nota do aluno {nome_aluno}: '))
nota2 = int(input(f'Digite a segunda nota do aluno {nome_aluno}: '))

media_nota = (nota1 + nota2) / 2

print(f'A média do aluno {nome_aluno} é {media_nota}')
