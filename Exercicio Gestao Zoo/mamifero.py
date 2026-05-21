from animal import Animal

class Mamifero(Animal):
    def __init__(self, nome, idade, especie, alimentacao):
        super().__init__(nome, idade, especie)
        self.alimentacao = alimentacao

    def mostrar_info(self):
        super().mostrar_info()
        print("Tipo de alimentação:", self.alimentacao)