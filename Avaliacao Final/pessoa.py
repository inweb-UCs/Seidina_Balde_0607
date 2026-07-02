from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, bi, nome, telefone):
        if not bi or not nome:
            raise ValueError("BI e Nome são obrigatórios.")

        self.__bi = bi
        self.__nome = nome
        self.__telefone = telefone

    def get_bi(self): return self.__bi
    def get_nome(self): return self.__nome
    def get_telefone(self): return self.__telefone

    def set_nome(self, nome):
        if nome.strip() == "":
            raise ValueError("Nome inválido.")
        self.__nome = nome

    def set_telefone(self, telefone):
        self.__telefone = telefone

    @abstractmethod
    def info(self):
        pass
