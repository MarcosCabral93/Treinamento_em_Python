"""
Filter

Filter( )-> Serve para filtrar dados de uma determiada coleção
Filter precisa de 2 parametros o primeiro é uma função e o segundo é um itervel

"""
import statistics

val=( 1,2,3,4,5,6)
media = (sum(val)/len(val))

#media com statistics
media=statistics.mean(val)




#utilizando filter
res=filter(lambda x: x> media, val )

paises=["Brasil", "", "Argentina", "EUA", "", "", "Alemanha"]

#paises=filter(lambda x: len(paises)>0, paises)
paises_filter=filter(None, paises)
print(list(paises_filter))

"""
Exemplo complexo
"""
user=[

    {"username": "marcos", "tweets":["eu amo voce", "I love you"]},
    {"username": "Joao", "tweets":["eu odeio voce", "I hate you"]},
    {"username": "jose", "tweets":["eu gosto voce",]},
    {"username": "lini", "tweets":[]},

    
]
#filtrar usuarios inativos
#forma 1
user_inativo=filter(lambda x: len(x['tweets']) ==0, user)
#forma 2 
user_inativo=filter(lambda x: not len(x['tweets']) , user)

print(list(user_inativo))