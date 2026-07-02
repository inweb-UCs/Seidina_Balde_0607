from pessoa import Pessoa

class Visitante(Pessoa):
    def __init__(self, bi, nome, telefone, idade):
        super().__init__(bi, nome, telefone)

        if idade < 0:
            raise ValueError("Idade inválida.")

        self.__idade = idade

    def get_idade(self): return self.__idade

    def set_idade(self, idade):
        if idade < 0:
            raise ValueError("Idade inválida.")
        self.__idade = idade

    def info(self):
        return f"{self.get_nome()} ({self.get_bi()}) - {self.__idade} anos"

    def to_dict(self):
        return {
            "bi": self.get_bi(),
            "nome": self.get_nome(),
            "telefone": self.get_telefone(),
            "idade": self.__idade
        }
