class Cliente:
    def __init__(self, id_cliente, nome, email):
        self.__id_cliente = id_cliente
        self.__nome = nome
        self.__email = email

    # GET
    def get_id(self):
        return self.__id_cliente

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    # SETTERS
    def set_nome(self, nome):
        self.__nome = nome

    def set_email(self, email):
        self.__email = email

    # INFO COMPLETA
    def info(self):
        return f"ID: {self.__id_cliente} | Nome: {self.__nome} | Email: {self.__email}"