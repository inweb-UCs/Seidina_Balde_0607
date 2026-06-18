class Pessoa:
    def __init__(self, bi, nome, telefone, email):
        self.__bi = None
        self.__nome = None
        self.__telefone = None
        self.__email = None

        self.set_bi(bi)
        self.set_nome(nome)
        self.set_telefone(telefone)
        self.set_email(email)

    def get_bi(self):
        return self.__bi

    def get_nome(self):
        return self.__nome

    def get_telefone(self):
        return self.__telefone

    def get_email(self):
        return self.__email

    def set_bi(self, bi):
        if not bi.strip():
            raise ValueError("BI não pode estar vazio.")
        self.__bi = bi.strip()

    def set_nome(self, nome):
        if len(nome.strip()) < 3:
            raise ValueError("O nome deve ter pelo menos 3 caracteres.")
        self.__nome = nome.strip()

    def set_telefone(self, telefone):
        if not telefone.isdigit() or len(telefone) != 9:
            raise ValueError("Telefone deve ter 9 dígitos.")
        self.__telefone = telefone

    def set_email(self, email):
        if "@" not in email or "." not in email:
            raise ValueError("Email inválido.")
        self.__email = email.strip()

    def info_completa(self):
        return f"BI: {self.__bi}, Nome: {self.__nome}, Telefone: {self.__telefone}, Email: {self.__email}"
