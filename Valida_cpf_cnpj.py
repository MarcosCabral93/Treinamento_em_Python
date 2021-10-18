from validate_docbr import CPF,CNPJ
class Documento:
    @staticmethod
    def cria_doc(dov):
        numero=str(dov)
        if len(numero) ==11:
            return Cpf(numero)

        elif len(numero)==14:
            return Cnpj(numero)
        else:
            raise ValueError("Você digitou um numero inválido")


class Cpf:
    def __init__(self, numero):
        
        if self.valida_numero(numero):
            self.cpf= numero
        else:
            raise ValueError("cpf inválido")
    def __str__(self):
        mascara=CPF()
        return mascara.mask(self.cpf)
    
    def valida_numero(self,numero):
        valida=CPF()
        return valida.validate(numero)


class Cnpj:
    def __init__(self,numero):
        if self.valida_numero(numero):
            self.cnpj=numero
        else:
            raise ValueError("CNPJ inválido")

    def __str__(self):
        mascara=CNPJ()
        return mascara.mask(self.cnpj)
    
    def valida_numero(self,numero):
        valida=CNPJ()
        return valida.validate(numero)
        






cpf1=Documento.cria_doc(15868910737)
print(cpf1)
cnpj1=Documento.cria_doc(30716847000138)
print(cnpj1)
