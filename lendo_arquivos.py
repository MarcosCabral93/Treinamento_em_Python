"""
Leitura de Arquivos

Para ler usamos o open()

open => forma mais utilizada é passando somente um parametro que é o arquivo a ser lido
A funcao retorna um _io.TextIOWrapper e é com ele que trabalahamos

"""
texto = open('oi.txt')
print(texto.read())