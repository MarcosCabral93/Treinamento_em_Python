import re

endereco="ola mundo sombrio: cep = 0 "

modelo= re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca=modelo.search(endereco) #se encontrou o padra, retorna a a string dele, se n encontrar retorna none
if busca:
    cep=busca.group()
    print(cep)
else:
    print("manda o Cep mocorongo!!!")