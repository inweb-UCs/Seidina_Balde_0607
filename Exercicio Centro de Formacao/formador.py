from pessoa import Pessoa

class Formador(Pessoa):
    def __init__(self, bi, nome, telefone, email, area_formacao):
        super().__init__(bi, nome, telefone, email)
        self.__area_formacao = None
        self.__ativo = True
        self.set_area_formacao(area_formacao)

    def get_area_formacao(self):
        return self.__area_formacao

    def is_ativo(self):
        return self.__ativo

    def set_area_formacao(self, area):
        if not area.strip():
            raise ValueError("Área de formação não pode estar vazia.")
        self.__area_formacao = area.strip()

    def desativar(self):
        self.__ativo = False

    def info_completa(self):
        estado = "Ativo" if self.__ativo else "Inativo"
        return f"{super().info_completa()}, Área: {self.__area_formacao}, Estado: {estado}"
