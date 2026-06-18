class Curso:
    def __init__(self, codigo, nome, area, duracao_horas, preco):
        self.__codigo = None
        self.__nome = None
        self.__area = None
        self.__duracao_horas = None
        self.__preco = None

        self.set_codigo(codigo)
        self.set_nome(nome)
        self.set_area(area)
        self.set_duracao_horas(duracao_horas)
        self.set_preco(preco)

    def get_codigo(self):
        return self.__codigo

    def get_nome(self):
        return self.__nome

    def get_area(self):
        return self.__area

    def get_duracao_horas(self):
        return self.__duracao_horas

    def get_preco(self):
        return self.__preco

    def set_codigo(self, codigo):
        if not codigo.strip():
            raise ValueError("Código não pode estar vazio.")
        self.__codigo = codigo.strip()

    def set_nome(self, nome):
        if len(nome.strip()) < 3:
            raise ValueError("Nome deve ter pelo menos 3 caracteres.")
        self.__nome = nome.strip()

    def set_area(self, area):
        if not area.strip():
            raise ValueError("Área não pode estar vazia.")
        self.__area = area.strip()

    def set_duracao_horas(self, duracao):
        dur = int(duracao)
        if dur <= 0:
            raise ValueError("Duração deve ser superior a zero.")
        self.__duracao_horas = dur

    def set_preco(self, preco):
        p = float(preco)
        if p < 0:
            raise ValueError("Preço não pode ser negativo.")
        self.__preco = p

    def info_completa(self):
        return f"Código: {self.__codigo}, Nome: {self.__nome}, Área: {self.__area}, Duração: {self.__duracao_horas}h, Preço: {self.__preco}€"
