"""
Com o map, fazemos mapeamento de valores para funcao
"""

import math

def area(r):
    """
    calcla a area de um circulo
    """
    return math.pi * (r**2)

raios=[11,5,6,8,7,9,1.5]

# print(list(map(area,raios)))


"""
Os maps são mais utilizados comfunclambdas

Porem so da para utilizar uma vez, pois depois ele zera limpando a memoria

"""
#Map com lambda
print(list(map(lambda r: math.pi * (r**2),raios)))
# Sintaxe map(1° parametro é uma funcao pode ser uma lambda ou uma funcao já declada, o segndo é um obeto iteravel)
# O resultado disso é um map Object

