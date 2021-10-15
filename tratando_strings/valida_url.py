import re
url='https://www.bytebanck.com.br/cambio'
padrao_url=re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cabio")
match=padrao_url.match(url)
padrao_url.match()