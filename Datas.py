class Data:
    def __init__(self,dia,mes,ano):
        self.dia=dia
        self.mes=mes
        self.ano=ano
    
    def data_formatada(self):
        print("{}/{}/{}".format(self.dia,self.mes,self.ano))
        
nova_data=Data(31,10,2018)
nova_data.data_formatada()