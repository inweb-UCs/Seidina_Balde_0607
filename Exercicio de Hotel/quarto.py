class Quarto:
    def __init__(self, numero, preco_noite):
        self.__numero = numero
        self.__preco_noite = preco_noite
        self.__ocupado = False

    # GET
    def get_numero(self):
        return self.__numero

    def get_preco(self):
        return self.__preco_noite

    def is_ocupado(self):
        return self.__ocupado

    # SET
    def set_preco(self, preco):
        self.__preco_noite = preco

    def set_ocupado(self, estado):
        self.__ocupado = estado

    # INFO COMPLETA
    def info(self):
        estado = "Ocupado" if self.__ocupado else "Livre"
        return f"Quarto {self.__numero} | {self.__preco_noite}€/noite | Estado: {estado}"