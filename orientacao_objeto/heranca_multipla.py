"""
Herança multipla
Possibilidade de uma classe herdas de multiplas classes

Multiderivacao Direta ou Multiderivacao indireta

"""

# multiderivacao direta

# class Ex1:
#     pass

# class Ex2:
#     pass 

# class Multideriva(Ex1, Ex2):
#     pass


# # Exemplo 2 - Multiderivacao Indireta

# class Base1:
#     pass

# class Base2(Base1):
#     pass 

# class Base3(Base2):
#     pass

# class Multi2(Base3):
    # pass 


"""
Nao importa se a derivacao e direta ou indireta, a classe que realizar a heranca herdara todos os atributios 
e metodos da super class
"""


"""
MRO

"""
class Animal:
    def __init__(self,nome):
        self.__nome=nome
    
    def cumprimentar(self):
        return f'Olá {self.__nome}'

class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def cumprimentar(self):
        return f'Eu sou o {self._Animal__nome} um animal terrestre'

class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def cumprimentar(self):
       return f'Eu sou o {self._Animal__nome} um animal aquatico'

class Hibrido(Terrestre, Aquatico):
    def __init__(self, nome):
        super().__init__(nome)

pinguin=Hibrido("HAppy Feet")
print(pinguin.cumprimentar())