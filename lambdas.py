"""
As labdas são funçoes anonimas

Sintaxe
inicia com a palavra reservada lambda

def func(x):
    return 3 *x+1



    é a mesma coisa que 


lambda x:3*x + 1
"""

lambda x:3*x + 1

"""
expressoes com muiltiplas entradas
"""
sem_parametro=lambda :"Bom dia!!!!"
um_parametro=lambda x : "bom dia {}".format(x)
dois_parametro=lambda x,y : "bom dia {} {}".format(x,y)
# nparams=lambda ..........: expression....

print(sem_parametro())
print(um_parametro("marcos"))
print(dois_parametro("marcos", "paulo"))