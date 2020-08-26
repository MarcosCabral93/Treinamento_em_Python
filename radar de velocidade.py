import random
radar= float(input('digite a velocida '))
if radar>80:
    print('Sua velocidade foi de {}km/h voce foi multado e sual multa é {}'.format(radar, (radar-80)*7))
else:
    print('{}km/h voce esta dentro do limite de velocidade'.format(radar))