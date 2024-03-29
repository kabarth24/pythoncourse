from time import sleep

def contador(inicio, fim, passo):
  print('-=' * 30)
  print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
  sleep(2.5)

  if inicio < fim:
    cont = inicio
    while cont <= fim:
      print(f'{cont} ', end='', flush=True)
      sleep(0.5)
      cont += passo
    print('FIM!!!')
  else:
    cont = inicio
    while cont >= fim:
      print(f'{cont} ', end='', flush=True)
      sleep(0.5)
      cont -= passo
    print('FIM!!!')


contador(1, 10, 1)
contador(10, 1, 2)

print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
f = int(input('Fim: '))
pas = int(input('Passo: '))
if pas == 0:
  pas = 1

contador(ini, f, pas)