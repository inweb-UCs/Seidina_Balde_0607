class Reserva:
    def __init__(self, id_reserva, cliente, quarto, noites):
        self.__id_reserva = id_reserva
        self.__cliente = cliente
        self.__quarto = quarto
        self.__noites = noites
        self.__ativa = True

    # GET
    def get_id(self):
        return self.__id_reserva

    def get_cliente(self):
        return self.__cliente

    def get_quarto(self):
        return self.__quarto

    def get_noites(self):
        return self.__noites

    def is_ativa(self):
        return self.__ativa

    # CALCULAR TOTAL
    def total(self):
        return self.__noites * self.__quarto.get_preco()

    # CANCELAR
    def cancelar(self):
        self.__ativa = False
        self.__quarto.set_ocupado(False)

    # INFO COMPLETA
    def info(self):
        estado = "Ativa" if self.__ativa else "Cancelada"
        return (f"Reserva {self.__id_reserva} | Cliente: {self.__cliente.get_nome()} | "
                f"Quarto: {self.__quarto.get_numero()} | Noites: {self.__noites} | "
                f"Total: {self.total()}€ | Estado: {estado}")