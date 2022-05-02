"""
Polimorfismo
"""

class Animal(object):
    def __init__(self,nome) :
        self.__nome=nome
    
    def falar(self):
        raise NotImplementedError("A classe filha precisa implementar essemetodo")

    def comer(self):
        print(f'{self.__nome } esta comendo')

class Gato (Animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def falar(self):
        print(f'{self._Animal__nome } fala miau')

class Cachorro (Animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def falar(self):
           print(f'{self._Animal__nome } fala au au ')

class Rato (Animal):
    def __init__(self, nome):
        super().__init__(nome)

cao=Cachorro("Marley")
felix=Gato("Felix")
ricotirico=Rato("ricotirico")

cao.comer()
cao.falar()

felix.falar()
felix.comer()

ricotirico.falar()
ricotirico.comer()
