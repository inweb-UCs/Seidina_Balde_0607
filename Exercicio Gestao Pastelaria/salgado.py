from produto import Produto

class Salgado(Produto):
    def __init__(self, id_produto, nome, preco, massa, tipo_preparacao):
        super().__init__(id_produto, nome, preco)
        self.__massa = massa
        self.__tipo_preparacao = tipo_preparacao

    def get_massa(self):
        return self.__massa

    def get_tipo_preparacao(self):
        return self.__tipo_preparacao

    def set_massa(self, massa):
        self.__massa = massa

    def set_tipo_preparacao(self, tipo):
        self.__tipo_preparacao = tipo

    def info(self):
        base = super().info()
        return base + f" | Tipo: Salgado | Massa: {self.__massa} | Preparação: {self.__tipo_preparacao}"
