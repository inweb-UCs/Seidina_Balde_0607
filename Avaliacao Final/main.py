import json

# Importação das classes (ficam na pasta modelos/)
from funcionario import Funcionario
from visitante import Visitante
from atracao import Atracao


# ============================================================
#                    SISTEMA DE GESTÃO
# ============================================================
class Sistema:
    def __init__(self):
        self.funcionarios = []
        self.visitantes = []
        self.atracoes = []

    # ------------------ MÉTODOS DE PESQUISA ------------------
    def procurar_funcionario(self, bi):
        return next((f for f in self.funcionarios if f.get_bi() == bi), None)

    def procurar_visitante(self, bi):
        return next((v for v in self.visitantes if v.get_bi() == bi), None)

    def procurar_atracao(self, codigo):
        return next((a for a in self.atracoes if a.get_codigo() == codigo), None)

    # ------------------ GUARDAR EM JSON ------------------
    def guardar(self):
        data = {
            "funcionarios": [f.to_dict() for f in self.funcionarios],
            "visitantes": [v.to_dict() for v in self.visitantes],
            "atracoes": [a.to_dict() for a in self.atracoes]
        }

        with open("dados/dados.json", "w") as f:
            json.dump(data, f, indent=4)

        print("✔ Dados guardados com sucesso.")

    # ------------------ CARREGAR DE JSON ------------------
    def carregar(self):
        try:
            with open("dados/dados.json", "r") as f:
                data = json.load(f)

            # Reconstrução dos funcionários
            self.funcionarios = [Funcionario(**f) for f in data["funcionarios"]]

            # Reconstrução dos visitantes
            self.visitantes = [Visitante(**v) for v in data["visitantes"]]

            # Reconstrução das atrações
            self.atracoes = []
            for a in data["atracoes"]:
                func = self.procurar_funcionario(a["funcionario"])
                atr = Atracao(a["codigo"], a["nome"], a["altura_min"], a["lotacao"], func)

                for bi in a["visitantes"]:
                    v = self.procurar_visitante(bi)
                    if v:
                        atr.adicionar_visitante(v)

                self.atracoes.append(atr)

            print("✔ Dados carregados com sucesso.")

        except FileNotFoundError:
            print("⚠ Nenhum ficheiro encontrado. Crie dados primeiro.")


# ============================================================
#                           MENU
# ============================================================
def menu():
    sistema = Sistema()

    while True:
        print("\n================ MENU PRINCIPAL ================")
        print("1 - Registar Funcionário")
        print("2 - Registar Visitante")
        print("3 - Criar Atração")
        print("4 - Adicionar Visitante a Atração")
        print("5 - Listar Funcionários")
        print("6 - Listar Visitantes")
        print("7 - Listar Atrações")
        print("8 - Informação de Atração")
        print("9 - Guardar Dados")
        print("10 - Carregar Dados")
        print("0 - Sair")
        print("================================================")

        op = input("Opção: ")

        # ------------------ REGISTAR FUNCIONÁRIO ------------------
        if op == "1":
            try:
                bi = input("BI: ")
                nome = input("Nome: ")
                tel = input("Telefone: ")
                funcao = input("Função: ")

                sistema.funcionarios.append(Funcionario(bi, nome, tel, funcao))
                print("✔ Funcionário registado.")
            except Exception as e:
                print("Erro:", e)

        # ------------------ REGISTAR VISITANTE ------------------
        elif op == "2":
            try:
                bi = input("BI: ")
                nome = input("Nome: ")
                tel = input("Telefone: ")
                idade = int(input("Idade: "))

                sistema.visitantes.append(Visitante(bi, nome, tel, idade))
                print("✔ Visitante registado.")
            except Exception as e:
                print("Erro:", e)

        # ------------------ CRIAR ATRAÇÃO ------------------
        elif op == "3":
            codigo = input("Código: ")
            nome = input("Nome: ")
            altura = int(input("Altura mínima: "))
            lotacao = int(input("Lotação máxima: "))
            bi_func = input("BI do Funcionário responsável: ")

            func = sistema.procurar_funcionario(bi_func)
            if func:
                sistema.atracoes.append(Atracao(codigo, nome, altura, lotacao, func))
                print("✔ Atração criada.")
            else:
                print("⚠ Funcionário não encontrado.")

        # ------------------ ADICIONAR VISITANTE ------------------
        elif op == "4":
            codigo = input("Código da atração: ")
            bi = input("BI do visitante: ")

            atr = sistema.procurar_atracao(codigo)
            vis = sistema.procurar_visitante(bi)

            if atr and vis:
                print("→", atr.adicionar_visitante(vis))
            else:
                print("⚠ Atração ou visitante não encontrado.")

        # ------------------ LISTAR FUNCIONÁRIOS ------------------
        elif op == "5":
            if not sistema.funcionarios:
                print("⚠ Nenhum funcionário registado.")
            for f in sistema.funcionarios:
                print(f.info())

        # ------------------ LISTAR VISITANTES ------------------
        elif op == "6":
            if not sistema.visitantes:
                print("⚠ Nenhum visitante registado.")
            for v in sistema.visitantes:
                print(v.info())

        # ------------------ LISTAR ATRAÇÕES ------------------
        elif op == "7":
            if not sistema.atracoes:
                print("⚠ Nenhuma atração registada.")
            for a in sistema.atracoes:
                print(f"{a.get_codigo()} - {a.get_nome()}")

        # ------------------ INFO ATRAÇÃO ------------------
        elif op == "8":
            codigo = input("Código: ")
            atr = sistema.procurar_atracao(codigo)
            print(atr.info() if atr else "⚠ Atração não encontrada.")

        # ------------------ GUARDAR ------------------
        elif op == "9":
            sistema.guardar()

        # ------------------ CARREGAR ------------------
        elif op == "10":
            sistema.carregar()

        # ------------------ SAIR ------------------
        elif op == "0":
            print("Programa terminado.")
            break

        else:
            print("⚠ Opção inválida.")


# Executar menu
if __name__ == "__main__":
    menu()
