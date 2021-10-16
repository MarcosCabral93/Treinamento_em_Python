valores=[5, 8, 42,9807,882]

# valores.append(75) # add no final
# print(valores)

valores.extend([5,71])# adiciona um iteravel a uma list
print(valores)

# for valor in valores:
#     nova_lisat.append(valor*2)
# print(nova_lisat)

nova_lista=[(item*2) for item in valores]
print(nova_lista
)
lista_Filtrada=[item for item in valores if item <50 ]
print(lista_Filtrada)
