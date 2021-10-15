url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100"
#Separa a url base e os parametros
parametro=url.find('?')
url_base=url[:parametro]
url_parametro=url[parametro+1:]


#exibindo o valor dos parametros
parametro_busca=('moedaDestino')
indice_parametro=url_parametro.find(parametro_busca)
#retorna o indice do valor 
indice_valor = indice_parametro+len(parametro_busca)+1
#verifica se ainda tem & nos parametros a partir do valor 
#se n houver ele retorna -1 
indice_e_com= url_parametro.find('&',indice_valor)
#exibe o valor do parametro
if indice_valor == -1:
    valor=url_parametro[indice_valor:]
else:
    valor=url_parametro[indice_valor:indice_e_com]


print(valor)







