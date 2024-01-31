times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG', )

cinco_primeiros_colocados = times[0:5]
ultimos_colocados = times[-4:]
times_em_ordem_alfabetica = tuple(sorted(times))
sao_paulo = times.index('São Paulo')

print(f'Os cinco primeiros colocados são: {cinco_primeiros_colocados}')
print(f'Os quatro últimos colocados são: {ultimos_colocados}')
print(f'Tabela em ordem alfabética: {times_em_ordem_alfabetica}')
print(f'O São Paulo está em {sao_paulo}º colocado')