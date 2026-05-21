from funcionario import Funcionario

class Programador(Funcionario):
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem

    def acao(self):
        print(self.nome, "está a programar em", self.linguagem)