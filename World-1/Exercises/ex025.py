distancia = float(
    input('Qual a distância da viagem que você está prestes a fazer? '))

viagem_curta = 200

viagens_curtas = 0.50
viagens_longas = 0.45

if distancia <= viagem_curta:
    valor_viagens_curtas = distancia * viagens_curtas
    print(
        f'Você está prestes a realizar uma viagem de curta distância, o valor da passsagem ficou R${valor_viagens_curtas:.2f}')
else:
    valor_viagens_longas = distancia * viagens_longas
    print(
        f'Você está prestes a realizar uma viagem de longa distância, o valor da passsagem ficou R${valor_viagens_longas:.2f}')
