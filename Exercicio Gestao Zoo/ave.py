from animal import Animal

class Ave(Animal):
    def __init__(self, nome, idade, especie, envergadura):
        super().__init__(nome, idade, especie)
        self.envergadura = envergadura

    def mostrar_info(self):
        super().mostrar_info()
        print("Envergadura das asas:", self.envergadura)