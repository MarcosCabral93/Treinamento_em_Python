dist=float(input('digite a distancia da sua viagem '))
if dist <= 200:
    print('O valor da sua viagem é R${}'.format(dist*0.50))
else:
    print('O valor da viagem é R${}'.format(dist*0.45))
