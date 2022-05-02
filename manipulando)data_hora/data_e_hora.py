"""
trabalhando com datas

"""
import datetime

# tempo1=datetime.datetime.now()
# print(tempo1)

# print("novo tempo ")
# tempo1=tempo1.replace(year=2023, hour=21, minute=0, second=0, microsecond=0)

# print(tempo1)


"""
Trabalhando com Delta de data e hora
data_inicial = dd/nn/yyyy 
data_final = dd/nn/yyyy 
delta= data_final-data_inicial
"""

# data_hj=datetime.datetime.now()
# data_final=datetime.datetime(2023,1,1)

# dias_faltantes=data_final-data_hj
# print(f'Faltam  {dias_faltantes.days} dias para seu niver!')

#Regra para vencimento Boleto
# data_compra=datetime.datetime.now()
# regra=datetime.timedelta(days=3)
# datapg=data_compra+regra
# print(datapg)

"""
Métodos de data e hora

"""
# agora=datetime.datetime.now() #com o now conseguimos parrar o fuso horario
# hoje=datetime.datetime.today()

"""
weekday()
dias da semana 
iniciando em 0 
 o 0 é a segunda-f

"""


"""
Formatando datas com strftime()

"""

dataat=datetime.datetime.now()
data_formatada=dataat.strftime("%d/%b/%Y")
print(data_formatada)

"""
Formatando datas com strptime()
coverte uma str em objeto datetime

"""
nascimento = datetime.datetime.strptime("1999/05/12", '%Y/%m/%d')
print(nascimento)