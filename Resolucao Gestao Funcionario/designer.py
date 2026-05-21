from funcionario import Funcionario

class Designer(Funcionario):
    def __init__(self, nome, salario, ferramenta):
        super().__init__(nome, salario)
        self.ferramenta = ferramenta

    def acao(self):
        print(self.nome, "está a criar design com", self.ferramenta)