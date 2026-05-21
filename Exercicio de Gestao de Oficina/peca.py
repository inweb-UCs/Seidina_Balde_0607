class Peca:
    def __init__(self, referencia, descricao):
        self.referencia = referencia
        self.descricao = descricao

    def mostrar(self):
        print("Referência:", self.referencia)
        print("Descrição:", self.descricao)