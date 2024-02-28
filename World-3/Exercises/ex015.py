from time import sleep

def maior(* num):
  print('-=' * 20)
  print('Analisando os valores passados...')
  for valor in num:
    print(f'{valor} ', end='', flush=True)
    sleep(0.5)
  
  print(f'Foram informados {len(num)} valores ao todo.')
  print(f'O maior valor informado foi {max(num)}')


maior(1, 5, 10, 15, 18, 14, 104)
maior(22, 7, 6, 64, 20)
maior(18, 48, 68, 28)
maior(120, 240)