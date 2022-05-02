"""
Trabalhando com listComprehension
Cria novas listas

Seintaxe
[dado for dado in iteravel]
Para compeensão devemos dividir em 2 partes 
A primeira parte : for x in n
a segunda parte : x+1

"""

# n=[1,2,3,3,4,5,6,7,8]
# new_list=[x+1 for x in n ]
# print(new_list)

"""
List comprehenson vs Loops
"""

n=[1,2,3,3,4,5,6,7,8]

# print([x+1 for x in n ])


# list_empty=[]
# for n in n:
#     n+=1
#     list_empty.append(n)
# print(list_empty)


"""
adicionando condicionais as lis comprehenson
"""
pares =[numero for numero in n if numero %2 ==0]
impares =[numero for numero in n if numero %2 !=0]
print(pares)
print(impares)