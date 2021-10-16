class Conta_corrent:
    def __init__(self, codigo):
        self.codigo=codigo
        self.saldo=0
    def deposita(self, valor):
        self.saldo+=valor
    def __str__(self):
        return "Codigo {} saldo: {}".format(self.codigo,self.saldo)
        
conta1=Conta_corrent(123)
conta2=Conta_corrent(321)
conta1.deposita(1000)
conta2.deposita(1579)
lista=[conta2,conta1]
for info in lista:
    print(info)