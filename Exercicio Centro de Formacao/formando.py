from pessoa import Pessoa

class Formando(Pessoa):
    def __init__(self, bi, nome, telefone, email, numero_formando):
        super().__init__(bi, nome, telefone, email)
        self.__numero_formando = None
        self.__ativo = True
        self.set_numero_formando(numero_formando)

    def get_numero_formando(self):
        return self.__numero_formando

    def is_ativo(self):
        return self.__ativo

    def set_numero_formando(self, numero):
        if not numero.strip():
            raise ValueError("Número de formando não pode estar vazio.")
        self.__numero_formando = numero.strip()

    def desativar(self):
        self.__ativo = False

    def info_completa(self):
        estado = "Ativo" if self.__ativo else "Inativo"
        return f"{super().info_completa()}, Nº Formando: {self.__numero_formando}, Estado: {estado}"
