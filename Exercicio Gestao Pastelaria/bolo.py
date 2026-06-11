from produto import Produto

class Bolo(Produto):
    def __init__(self, id_produto, nome, preco, recheio, fatias):
        super().__init__(id_produto, nome, preco)
        self.__recheio = recheio
        self.__fatias = fatias

    def get_recheio(self):
        return self.__recheio

    def get_fatias(self):
        return self.__fatias

    def set_recheio(self, recheio):
        self.__recheio = recheio

    def set_fatias(self, fatias):
        self.__fatias = fatias

    def info(self):
        base = super().info()
        return base + f" | Tipo: Bolo | Recheio: {self.__recheio} | Fatias: {self.__fatias}"
