"""
Metodo Super Refere-se a super classe 
"""

class Animal:
    def __init__(self,nome, especie):
        self.__nome=nome
        self.__especie=especie

    def som(self, som):
        print(f'O {self.__nome}  faz {som} ')

class Cachorro(Animal):
    def __init__(self, nome, especie, raca):
        #Modo correto de invocar a classe mae 
        super().__init__(nome, especie)
        #modo possivel, porem nao recomendado
        # Animal.__init__(self,nome, especie)
        self.__raca=raca

cachorro1=Cachorro("marley", "Cachorro", "Labrador")
cachorro1.som("au au")