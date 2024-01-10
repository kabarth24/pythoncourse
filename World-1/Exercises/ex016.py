nome_completo = str(input('Digite o seu nome completo: ')).strip()

letras_maiusculas = nome_completo.upper()
letras_minusculas = nome_completo.lower()
comprimento_nome_sem_espacos = len(nome_completo) - nome_completo.count(' ')
comprimento = nome_completo.split()
primeiro_nome = len(comprimento[0])

print(f'Seu nome em maiúsculas é {letras_maiusculas}')
print(f'Seu nome em minúsculas é {letras_minusculas}')
print(f'Seu nome tem ao todo {comprimento_nome_sem_espacos} letras')
print(f'Seu primeiro nome tem {primeiro_nome} letras')
