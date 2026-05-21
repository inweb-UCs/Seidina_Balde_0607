class Proprietario:
    def __init__(self, nif, nome, morada):
        self.nif = nif
        self.nome = nome
        self.morada = morada

    def mostrar(self):
        print("NIF:", self.nif)
        print("Nome:", self.nome)
        print("Morada:", self.morada)