class Produto:
    def __init__(self, id_produto, nome, preco):
        self.__id = id_produto
        self.__nome = nome
        self.__preco = preco

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def set_nome(self, nome):
        self.__nome = nome

    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco

    def info(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | Preço: {self.__preco:.2f}€"
