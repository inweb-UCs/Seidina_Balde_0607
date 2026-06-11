class Producao:
    def __init__(self, produto, quantidade, data):
        self.__produto = produto
        self.__quantidade = quantidade
        self.__data = data

    def get_produto(self):
        return self.__produto

    def get_quantidade(self):
        return self.__quantidade

    def get_data(self):
        return self.__data

    def set_quantidade(self, nova_qtd):
        if nova_qtd > 0:
            self.__quantidade = nova_qtd

    def valor_total(self):
        return self.__quantidade * self.__produto.get_preco()

    def info(self):
        return (f"Produto: {self.__produto.get_nome()} | Quantidade: {self.__quantidade} | "
                f"Data: {self.__data} | Valor Total: {self.valor_total():.2f}€")
