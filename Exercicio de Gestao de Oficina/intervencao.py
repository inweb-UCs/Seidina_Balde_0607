class Intervencao:
    def __init__(self, veiculo, data):
        self.veiculo = veiculo
        self.data = data
        self.pecas = []

    def adicionar_peca(self, peca):
        self.pecas.append(peca)

    def mostrar(self):
        print("Data:", self.data)
        print("Veículo:", self.veiculo.matricula)
        print("Peças utilizadas:")
        for p in self.pecas:
            print("-", p.descricao)