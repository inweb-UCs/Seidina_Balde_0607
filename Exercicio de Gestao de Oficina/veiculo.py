class Veiculo:
    def __init__(self, proprietario, matricula, marca, modelo):
        self.proprietario = proprietario
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo

    def mostrar(self):
        print("Matrícula:", self.matricula)
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Proprietário:", self.proprietario.nome)