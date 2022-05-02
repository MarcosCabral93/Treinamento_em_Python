"""
Propriedades 
"""

#Forma1

# class Conta:
#     contador=0

#     def __init__(self, titular, saldo , limite):
#         self.__titular=titular
#         self.__saldo=saldo
#         self.__limite=limite
#         Conta.contador+=1
    
#     def extrato(self):
#         return f"O seusaldo é de R$ {self.__saldo}"

#     def sacar(self,valor):
#         self.__saldo -= valor       
    
#     def depositar(self,valor):
#         self.__saldo += valor   

#     def get_saldo(self):
#         return self.__saldo    

#     def set_saldo(self,new_saldo):
#         self.__saldo=new_saldo
        
    
# conta1=Conta("Marcos",3000, 5000)
# conta2=Conta("Paulo",4000, 2000)

# conta1.extrato()



class Conta:
    contador=0

    def __init__(self, titular, saldo , limite):
        self.__titular=titular
        self.__saldo=saldo
        self.__limite=limite
        Conta.contador+=1

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, new_value):
        self.__limite=new_value
    
    def extrato(self):
        return f"O seusaldo é de R$ {self.__saldo}"

    def sacar(self,valor):
        self.__saldo -= valor       
    
    def depositar(self,valor):
        self.__saldo += valor   

    def get_saldo(self):
        return self.__saldo    

    def set_saldo(self,new_saldo):
        self.__saldo=new_saldo
        
    
conta1=Conta("Marcos",3000, 5000)
conta2=Conta("Paulo",4000, 2000)

conta1.extrato()
print(conta1.limite)
conta1.limite=5787
print(conta1.limite)