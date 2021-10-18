import re 

class Telefone:
    def __init__(self,telefone):
        if self.valida_numero(telefone):
            self.telefone=telefone
        else:
            raise ValueError("Número invalido")
    def valida_numero(self,telefone):
        padrao="([0-9] {2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        r=re.findall(padrao,telefone)
        if r:
            return True
        else:
            return False
    def __str__(self):
        padrao="([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        r=re.search(padrao,self.telefone)
        tel="+ {} {} {}-{}".format(r.group(1),r.group(2),r.group(3),r.group(4))
        return tel

telegone=Telefone('5521980484585')
print(telegone)
    