"""
funcoes com parametro
"""

def quadrado(n):
    return n*n

quadrado(8)

"""
Parametros e Argumentos

"""
def read_name(name,last_name): #parametros da func
    print(name,last_name)

read_name("Marcos", "Cabral") #argumentos da func

"""
Argumnetos Nomeados
"""

read_name(name="Marcos", last_name="Cabral") #argumentos da func nomeados

"""
O return interrompe a funcao
"""

"""
definindo func com argumento padrao
"""
def arg_padrao(n, pow=2):
    return n ** pow

arg_padrao(5,5)
arg_padrao(5)


"""
Documentando funcoes com docstring
"""

def documentando_func(n):
    """
    Funçao que retorna o quadrado de um numero
    n: Número escolhido
    """
    return n **2

"""
Entendendo o args
"""
def test_args(n1,n2,n3):
    return n1+n2+n3
test_args(1,2)