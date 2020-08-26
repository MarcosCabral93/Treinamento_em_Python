import random
n = int(random.randrange(0,5))
nu= int(input('Digite um numero entre 0 e 5 '))
if nu==n:
    print('O computador escolheu {} e voce {}. Voce Venceu'.format(n,nu))
else:
    print('o computador escolheu {} e voce {}. O Comp Venceu' .format(n,nu))