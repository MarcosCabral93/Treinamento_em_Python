class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor
    def transferir(self,valor,destino):
        self.sacar(valor)
        destino.depositar(valor)

    def get_numero(self):
        return self.__numero
    def get_titular(self):
        return self.__titular
    def get_limite(self):
        return self.__limite
    def set_limite(self,new_limite):
        self.__limite=new_limite
    
    #Usando Property
    @property
    def limite(self):
        print(" Exibindo limite Usando Property",self.__limite)
        return self.__limite
    @limite.setter
    def limite(self,new_limite):
        self.__limite=new_limite
        print(" Alteração usando Usando Property")




conta1=Conta(123,"Marcos",1000,1000)
conta2=Conta(321,"Lucas",1000,1000)

#Usando Property
conta1.limite
conta1.limite=1900
conta1.limite


# print("Sua conta tem limite de ",conta1.get_limite())
# conta1.set_limite(1500)
# print("Sua conta tem limite de ",conta1.get_limite())




# Trabalhando o metodo transferir

# conta1.transferir(100.0,conta2)
# conta1.extrato()
# conta2.extrato()
