nome_completo = str(input('Digite o seu nome completo: ')).strip()

nome_separado = nome_completo.split()

primeiro_nome = nome_separado[0].capitalize()
ultimo_nome = nome_separado[-1].capitalize()

print('Prazer em te conhecer!')
print(f'O seu primeiro nome é {primeiro_nome}')
print(f'O seu último nome é {ultimo_nome}')
