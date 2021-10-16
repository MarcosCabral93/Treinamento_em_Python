from collections import defaultdict,Counter

nome_idade={"Marcos":27, "paulo":10, 'larissa':18, 'paula':27}
for elemento in nome_idade.items():
    print(elemento)

frase="""eu sou muito legal, tambem sou bacaninha.
 eu sou muito chato as vezes  tambem. sou estudioso e as vezes preguiçoso"""

frase=frase.lower()
# dicionario_novo=defaultdict(int)
# for elem in :
#     dicionario_novo[elem]+=1
# print(dicionario_novo)
#Jaconta e poe o zero como padrao
novo_di=Counter(frase.split())
print(novo_di)
