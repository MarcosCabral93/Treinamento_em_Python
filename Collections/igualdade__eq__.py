class Conta:
    def __init__(self,conta):
        self.conta=conta
        self.saldo=0
    def __eq__(self, outro):
        return self.conta == outro.conta
conta1=Conta(123)
conta2=Conta(123)

v_f=conta1==conta2
print(v_f)




