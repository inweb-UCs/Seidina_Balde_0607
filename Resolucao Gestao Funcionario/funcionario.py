class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def mostrar_info(self):
        print("Nome:", self.nome)
        print("Salário:", self.salario)