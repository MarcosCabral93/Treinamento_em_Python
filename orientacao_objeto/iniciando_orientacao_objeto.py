"""

POO-Classes

Classes são modelos dos objetos do mundo real sendo representados computacionalmente

Classes podem conter :

- Atributos=> Representam caracteristicas do objeto, ou seja, pelos atributos conseguimos represntar os estados de um objetos.
Ex: lampadada é 110v ou 220v?
- Metodos=> 
Em python todo atributo da classe é publico
Por convencao atributos privados sao chamaso okuber 
usamos __ antes de declarar os metodos
Metodos de classe( conhecidos como métodos estaticos em outras linguagens) não acessam os atributos de instancia

Objetos=>
São instancias da classe

Encapsulamento e Abstração =>
O grande objetivo da POO é encapsular nosso codigo dentro de um grupo lógico e hierarquico utiliando classes

Abstracao=> ato de expor apenas dados relevantes de uma classe escondendo atributos e metodos privados de usuario

"""


# class Aluno:

#     @classmethod
#     def func_clase(cls):
#         print("Eu sou um att de classe")

#     # metodo construtor
#     def __init__(self, nome, matricula):
#         self.__nome = nome
#         self.__matricula = matricula
    
#     def canta(self):
#         return f'{self.__nome} cantou bonitoo'

# aluno1 = Aluno('Marcos', '123456')
# # print(aluno1.canta())

# Aluno.func_clase() #forma correta 
# aluno1.func_clase() # forma incorreta


#_____________________________________________________
#Objetos

from matplotlib.pyplot import cla


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor=cor
        self.__voltagem=voltagem
        self.__luminosidade=luminosidade
        self.__luminosidade=False

#instancia
lamp1= Lampada('verde', 110, 60)

#_____________________________
#Encapsulamento e Abstração

class Conta:
    contador = 400

    def __init__(self,titular, saldo,limite):
        self._numero=Conta.contador
        self._titular=titular 
        self._saldo=saldo
        self._limite=limite
        Conta.contador+=1

    def extrato(self):
        print(f'O saldo atuaç é {self._saldo}')


    def depositar(self,valor):
        self._saldo+=valor


    def sacar(self,valor):
         self._saldo-=valor

cc1= Conta("MArcos", 150, 1500)
cc1.depositar(200)