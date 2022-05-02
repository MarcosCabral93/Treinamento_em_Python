"""
Heranca (inheritence)
Ideia de reaproveitar codigo e exetender classes 
"""
"""
Forma não orientada a Obj

class Cliente:
    def __init__(self, nome, sobrenome, cpf, conta):
        self.__nome=nome
        self.__sobrenome=sobrenome
        self.__cpf=cpf
        self.__conta=conta

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Funcionario:
    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome=nome
        self.__sobrenome=sobrenome
        self.__cpf=cpf
        self.matricula=matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
        """

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome=nome
        self.__sobrenome=sobrenome
        self.__cpf=cpf
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf, conta):
        super().__init__(nome, sobrenome, cpf)
        self.__conta=conta

  

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__( nome, sobrenome, cpf)
        self.__matricula=matricula

novo_cliente= Cliente("Marcos", "cabral",15868910737,555668)
novo_funcionario= Funcionario("ola", "mundo",15868910737,555668)


print(novo_cliente.nome_completo())