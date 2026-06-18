from formando import Formando
from formador import Formador
from curso import Curso
from turma import Turma

# ============================================================
# LISTAS DE DADOS
# ============================================================

formandos = []
formadores = []
cursos = []
turmas = []

# ============================================================
# FUNÇÕES DE PESQUISA
# ============================================================

def procurar_formando_bi(bi):
    return next((f for f in formandos if f.get_bi() == bi), None)

def procurar_formando_numero(num):
    return next((f for f in formandos if f.get_numero_formando() == num), None)

def procurar_formador_bi(bi):
    return next((f for f in formadores if f.get_bi() == bi), None)

def procurar_curso_codigo(cod):
    return next((c for c in cursos if c.get_codigo() == cod), None)

def procurar_turma_codigo(cod):
    return next((t for t in turmas if t.get_codigo() == cod), None)

# ============================================================
# OPERAÇÕES DO SISTEMA
# ============================================================

def registar_formando():
    print("\n--- Registar Formando ---")
    try:
        bi = input("BI: ").strip()
        if procurar_formando_bi(bi):
            print("Já existe um formando com esse BI.")
            return

        nome = input("Nome: ").strip()
        telefone = input("Telefone: ").strip()
        email = input("Email: ").strip()
        numero = input("Número de formando: ").strip()

        if procurar_formando_numero(numero):
            print("Já existe um formando com esse número.")
            return

        novo = Formando(bi, nome, telefone, email, numero)
        formandos.append(novo)
        print("Formando registado com sucesso.")
    except Exception as e:
        print("Erro:", e)


def registar_formador():
    print("\n--- Registar Formador ---")
    try:
        bi = input("BI: ").strip()
        if procurar_formador_bi(bi):
            print("Já existe um formador com esse BI.")
            return

        nome = input("Nome: ").strip()
        telefone = input("Telefone: ").strip()
        email = input("Email: ").strip()
        area = input("Área de formação: ").strip()

        novo = Formador(bi, nome, telefone, email, area)
        formadores.append(novo)
        print("Formador registado com sucesso.")
    except Exception as e:
        print("Erro:", e)


def registar_curso():
    print("\n--- Registar Curso ---")
    try:
        codigo = input("Código: ").strip()
        if procurar_curso_codigo(codigo):
            print("Já existe um curso com esse código.")
            return

        nome = input("Nome: ").strip()
        area = input("Área: ").strip()
        duracao = input("Duração (horas): ").strip()
        preco = input("Preço: ").strip()

        novo = Curso(codigo, nome, area, duracao, preco)
        cursos.append(novo)
        print("Curso registado com sucesso.")
    except Exception as e:
        print("Erro:", e)


def criar_turma():
    print("\n--- Criar Turma ---")
    try:
        codigo = input("Código da turma: ").strip()
        if procurar_turma_codigo(codigo):
            print("Já existe uma turma com esse código.")
            return

        cod_curso = input("Código do curso: ").strip()
        curso = procurar_curso_codigo(cod_curso)
        if not curso:
            print("Curso não encontrado.")
            return

        bi_formador = input("BI do formador: ").strip()
        formador = procurar_formador_bi(bi_formador)
        if not formador:
            print("Formador não encontrado.")
            return
        if not formador.is_ativo():
            print("Formador inativo.")
            return

        data = input("Data de início: ").strip()
        lotacao = input("Lotação máxima: ").strip()

        nova = Turma(codigo, curso, formador, data, lotacao)
        turmas.append(nova)
        print("Turma criada com sucesso.")
    except Exception as e:
        print("Erro:", e)


def inscrever_formando():
    print("\n--- Inscrever Formando ---")
    try:
        cod_turma = input("Código da turma: ").strip()
        turma = procurar_turma_codigo(cod_turma)
        if not turma:
            print("Turma não encontrada.")
            return

        bi = input("BI do formando: ").strip()
        formando = procurar_formando_bi(bi)
        if not formando:
            print("Formando não encontrado.")
            return

        turma.inscrever(formando)
        print("Formando inscrito com sucesso.")
    except Exception as e:
        print("Erro:", e)


def listar_formandos():
    print("\n--- Lista de Formandos ---")
    if not formandos:
        print("Nenhum formando registado.")
        return
    for f in formandos:
        print(f.info_completa())


def listar_formadores():
    print("\n--- Lista de Formadores ---")
    if not formadores:
        print("Nenhum formador registado.")
        return
    for f in formadores:
        print(f.info_completa())


def listar_cursos():
    print("\n--- Lista de Cursos ---")
    if not cursos:
        print("Nenhum curso registado.")
        return
    for c in cursos:
        print(c.info_completa())


def listar_turmas():
    print("\n--- Lista de Turmas ---")
    if not turmas:
        print("Nenhuma turma registada.")
        return
    for t in turmas:
        print(t.info_completa())


def info_formando():
    bi = input("BI do formando: ").strip()
    f = procurar_formando_bi(bi)
    if not f:
        print("Formando não encontrado.")
        return

    print("\n" + f.info_completa())
    print("\nTurmas inscritas:")
    encontrou = False
    for t in turmas:
        if f in t.get_formandos():
            print(f"- {t.get_codigo()} ({t.get_curso().get_nome()})")
            encontrou = True
    if not encontrou:
        print("Nenhuma.")


def info_formador():
    bi = input("BI do formador: ").strip()
    f = procurar_formador_bi(bi)
    if not f:
        print("Formador não encontrado.")
        return

    print("\n" + f.info_completa())
    print("\nTurmas que leciona:")
    encontrou = False
    for t in turmas:
        if t.get_formador() == f:
            print(f"- {t.get_codigo()} ({t.get_curso().get_nome()})")
            encontrou = True
    if not encontrou:
        print("Nenhuma.")


def info_curso():
    cod = input("Código do curso: ").strip()
    c = procurar_curso_codigo(cod)
    if not c:
        print("Curso não encontrado.")
        return

    print("\n" + c.info_completa())
    print("\nTurmas associadas:")
    total = 0
    encontrou = False
    for t in turmas:
        if t.get_curso() == c:
            print(f"- {t.get_codigo()} ({len(t.get_formandos())} formandos)")
            total += len(t.get_formandos())
            encontrou = True
    if not encontrou:
        print("Nenhuma.")
    print(f"\nTotal de formandos inscritos: {total}")


def info_turma():
    cod = input("Código da turma: ").strip()
    t = procurar_turma_codigo(cod)
    if not t:
        print("Turma não encontrada.")
        return

    print("\n" + t.info_completa())
    print("\nCurso:")
    print(t.get_curso().info_completa())
    print("\nFormador:")
    print(t.get_formador().info_completa())
    print("\nFormandos:")
    if not t.get_formandos():
        print("Nenhum.")
    else:
        for f in t.get_formandos():
            print(f"- {f.get_nome()} ({f.get_bi()})")


def alterar_estado():
    cod = input("Código da turma: ").strip()
    t = procurar_turma_codigo(cod)
    if not t:
        print("Turma não encontrada.")
        return

    print("Estados permitidos:", ", ".join(Turma.ESTADOS))
    novo = input("Novo estado: ").strip()

    try:
        t.alterar_estado(novo)
        print("Estado alterado com sucesso.")
    except Exception as e:
        print("Erro:", e)


def receita_total():
    total = sum(t.receita_prevista() for t in turmas if t.get_estado() != "cancelada")
    print(f"\nReceita total prevista: {total}€")

# ============================================================
# MENU PRINCIPAL
# ============================================================

def mostrar_menu():
    print("\n--- Plataforma Centro de Formação ---")
    print("1 - Registar Formando")
    print("2 - Registar Formador")
    print("3 - Registar Curso")
    print("4 - Criar Turma")
    print("5 - Inscrever Formando")
    print("6 - Listar Formandos")
    print("7 - Listar Formadores")
    print("8 - Listar Cursos")
    print("9 - Listar Turmas")
    print("10 - Informação Formando")
    print("11 - Informação Formador")
    print("12 - Informação Curso")
    print("13 - Informação Turma")
    print("14 - Alterar Estado")
    print("15 - Receita Total")
    print("0 - Sair")

def main():
    while True:
        mostrar_menu()
        op = input("Opção: ")

        funcoes = {
            "1": registar_formando,
            "2": registar_formador,
            "3": registar_curso,
            "4": criar_turma,
            "5": inscrever_formando,
            "6": listar_formandos,
            "7": listar_formadores,
            "8": listar_cursos,
            "9": listar_turmas,
            "10": info_formando,
            "11": info_formador,
            "12": info_curso,
            "13": info_turma,
            "14": alterar_estado,
            "15": receita_total
        }

        if op == "0":
            print("A sair...")
            break

        func = funcoes.get(op)
        if func:
            func()
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
