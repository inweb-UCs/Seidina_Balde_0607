from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, bi, nome, telefone, funcao, ativo=True):
        super().__init__(bi, nome, telefone)
        self.__funcao = funcao
        self.__ativo = ativo

    def get_funcao(self): return self.__funcao
    def get_ativo(self): return self.__ativo

    def set_funcao(self, funcao):
        if funcao.strip() == "":
            raise ValueError("Função inválida.")
        self.__funcao = funcao

    def set_ativo(self, ativo):
        self.__ativo = ativo

    def info(self):
        return f"{self.get_nome()} ({self.get_bi()}) - {self.__funcao} - {'Ativo' if self.__ativo else 'Inativo'}"

    def to_dict(self):
        return {
            "bi": self.get_bi(),
            "nome": self.get_nome(),
            "telefone": self.get_telefone(),
            "funcao": self.__funcao,
            "ativo": self.__ativo
        }
