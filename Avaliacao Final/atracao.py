class Atracao:
    def __init__(self, codigo, nome, altura_min, lotacao, funcionario):
        if not codigo or not nome:
            raise ValueError("Código e nome são obrigatórios.")

        if altura_min < 0 or lotacao <= 0:
            raise ValueError("Altura mínima ou lotação inválida.")

        self.__codigo = codigo
        self.__nome = nome
        self.__altura_min = altura_min
        self.__lotacao = lotacao
        self.__funcionario = funcionario
        self.__visitantes = []

    def get_codigo(self): return self.__codigo
    def get_nome(self): return self.__nome
    def get_funcionario(self): return self.__funcionario
    def get_visitantes(self): return self.__visitantes

    def adicionar_visitante(self, visitante):
        if visitante.get_idade() < 5:
            return "Visitante demasiado jovem."

        if len(self.__visitantes) >= self.__lotacao:
            return "Lotação esgotada."

        self.__visitantes.append(visitante)
        return "Visitante adicionado."

    def info(self):
        texto = f"Atração {self.__nome} ({self.__codigo})\n"
        texto += f"Funcionário responsável: {self.__funcionario.get_nome()}\n"
        texto += "Visitantes:\n"
        for v in self.__visitantes:
            texto += f" - {v.get_nome()} ({v.get_idade()} anos)\n"
        return texto

    def to_dict(self):
        return {
            "codigo": self.__codigo,
            "nome": self.__nome,
            "altura_min": self.__altura_min,
            "lotacao": self.__lotacao,
            "funcionario": self.__funcionario.get_bi(),
            "visitantes": [v.get_bi() for v in self.__visitantes]
        }
