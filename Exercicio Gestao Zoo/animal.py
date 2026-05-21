class Animal:
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.consultas = []

    def mostrar_info(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Espécie:", self.especie)

    def mostrar_ficha_medica(self):
        self.mostrar_info()
        print("Consultas:")
        for c in self.consultas:
            print("-", c)

    def registar_consulta(self, consulta):
        self.consultas.append(consulta)