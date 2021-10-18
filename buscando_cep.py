import requests
class Cep:
    def __init__(self,numero):
        if self.valida_cep(numero):
            self.cep= str(numero)
        else:
            raise ValueError("Cep inválido")

    def valida_cep(self,numero):
        if len(numero):
            return True
        else:
            return False
    def __str__(self):
        return "{}-{}".format(self.cep[0:5],self.cep[5:])

    def consulta_endereco_cep(self):
        url= "http://viacep.com.br/ws/{}/json/".format(self.cep)
        r=requests.get(url)
        dados=r.json()
        return(
            dados['bairro'],
            dados['uf'],
            dados['localidade'])
            

        
novo_cep=Cep('23573260')

bairro,uf,localidade=novo_cep.consulta_endereco_cep()
print(bairro)
print(uf)
print(localidade)