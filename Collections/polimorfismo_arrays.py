class Conta:
    def __init__(self,conta):
        self._conta=conta
        self._saldo=0
    
    def deposita(self,valor):
        self._saldo+=valor

    def __str__(self):
        return "Conta:{} Saldo:{}".format(self._conta,self._saldo)

class Conta_corrente(Conta):
    def att_mensal(self):
        self._saldo-=2

class Conta_poupanca(Conta):
    def att_mensal(self):
        self._saldo*= 1.01
        self._saldo-=3
    
contap=Conta_poupanca(123)
contap.deposita(1000)
contap.att_mensal()
contac=Conta_corrente(321)
contac.deposita(1000)
contac.att_mensal()
contas=[contac,contap]
for conta in contas:
    print(conta)