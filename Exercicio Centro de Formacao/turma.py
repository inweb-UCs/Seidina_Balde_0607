class Turma:
    ESTADOS = ["planeada", "em funcionamento", "concluída", "cancelada"]

    def __init__(self, codigo, curso, formador, data_inicio, lotacao_maxima):
        self.__codigo = codigo
        self.__curso = curso
        self.__formador = formador
        self.__data_inicio = data_inicio
        self.__lotacao_maxima = int(lotacao_maxima)
        self.__estado = "planeada"
        self.__formandos = []

        if self.__lotacao_maxima <= 0:
            raise ValueError("Lotação deve ser superior a zero.")

    def get_codigo(self):
        return self.__codigo

    def get_curso(self):
        return self.__curso

    def get_formador(self):
        return self.__formador

    def get_formandos(self):
        return list(self.__formandos)

    def get_estado(self):
        return self.__estado

    def inscrever(self, formando):
        if self.__estado in ["concluída", "cancelada"]:
            raise ValueError("Turma não permite inscrições.")
        if len(self.__formandos) >= self.__lotacao_maxima:
            raise ValueError("Turma cheia.")
        if not formando.is_ativo():
            raise ValueError("Formando inativo.")
        if formando in self.__formandos:
            raise ValueError("Formando já inscrito.")
        self.__formandos.append(formando)

    def alterar_estado(self, estado):
        if estado not in Turma.ESTADOS:
            raise ValueError("Estado inválido.")
        self.__estado = estado

    def receita_prevista(self):
        return len(self.__formandos) * self.__curso.get_preco()

    def info_completa(self):
        return f"Turma {self.__codigo}, Curso: {self.__curso.get_nome()}, Formador: {self.__formador.get_nome()}, Estado: {self.__estado}, Inscritos: {len(self.__formandos)}/{self.__lotacao_maxima}"
