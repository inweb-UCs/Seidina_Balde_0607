from bolo import Bolo
from salgado import Salgado
from producao import Producao

# LISTAS DO SISTEMA
produtos = []
producoes = []

# MÉTODO DE PESQUISA (exigido pelo enunciado)
def procurar_produto(id_produto):
    for p in produtos:
        if p.get_id() == id_produto:
            return p
    return None

def producoes_do_produto(produto):
    return [p for p in producoes if p.get_produto().get_id() == produto.get_id()]


# ---------------- MENU ----------------

def menu():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1 - Registar Bolo")
        print("2 - Registar Salgado")
        print("3 - Registar Produção")
        print("4 - Listar Produtos")
        print("5 - Listar Produções")
        print("6 - Informação de Produto")
        print("7 - Alterar Preço de Produto")
        print("8 - Alterar Quantidade Produzida")
        print("9 - Receita Total Prevista")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            registar_bolo()
        elif opcao == "2":
            registar_salgado()
        elif opcao == "3":
            registar_producao()
        elif opcao == "4":
            listar_produtos()
        elif opcao == "5":
            listar_producoes()
        elif opcao == "6":
            info_produto()
        elif opcao == "7":
            alterar_preco()
        elif opcao == "8":
            alterar_quantidade()
        elif opcao == "9":
            receita_total()
        elif opcao == "0":
            print("A sair...")
            break
        else:
            print("Opção inválida.")


# ---------------- FUNÇÕES DO MENU ----------------

def registar_bolo():
    print("\n--- Registar Bolo ---")
    idp = input("ID: ")
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    recheio = input("Recheio: ")
    fatias = int(input("Número de fatias: "))

    produtos.append(Bolo(idp, nome, preco, recheio, fatias))
    print("Bolo registado!")


def registar_salgado():
    print("\n--- Registar Salgado ---")
    idp = input("ID: ")
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    massa = input("Tipo de massa: ")
    tipo = input("Frito ou Assado: ")

    produtos.append(Salgado(idp, nome, preco, massa, tipo))
    print("Salgado registado!")


def registar_producao():
    print("\n--- Registar Produção ---")
    idp = input("ID do produto: ")

    produto = procurar_produto(idp)
    if not produto:
        print("Produto não encontrado.")
        return

    quantidade = int(input("Quantidade produzida: "))
    if quantidade <= 0:
        print("Quantidade inválida.")
        return

    data = input("Data de produção: ")
    if data.strip() == "":
        print("Data inválida.")
        return

    producoes.append(Producao(produto, quantidade, data))
    print("Produção registada!")


def listar_produtos():
    print("\n--- Lista de Produtos ---")
    if not produtos:
        print("Nenhum produto registado.")
        return

    for p in produtos:
        print(p.info())


def listar_producoes():
    print("\n--- Lista de Produções ---")
    if not producoes:
        print("Nenhuma produção registada.")
        return

    for p in producoes:
        print(p.info())


def info_produto():
    idp = input("ID do produto: ")
    produto = procurar_produto(idp)

    if not produto:
        print("Produto não encontrado.")
        return

    print("\n" + produto.info())
    print("\nProduções associadas:")

    assoc = producoes_do_produto(produto)
    if not assoc:
        print("Nenhuma produção.")
    else:
        for p in assoc:
            print(p.info())


def alterar_preco():
    idp = input("ID do produto: ")
    produto = procurar_produto(idp)

    if not produto:
        print("Produto não encontrado.")
        return

    novo = float(input("Novo preço: "))
    if novo < 0:
        print("Preço inválido.")
        return

    produto.set_preco(novo)
    print("Preço atualizado!")


def alterar_quantidade():
    listar_producoes()
    indice = int(input("Número da produção (1..n): ")) - 1

    if indice < 0 or indice >= len(producoes):
        print("Produção inválida.")
        return

    nova = int(input("Nova quantidade: "))
    if nova <= 0:
        print("Quantidade inválida.")
        return

    producoes[indice].set_quantidade(nova)
    print("Quantidade atualizada!")


def receita_total():
    total = sum(p.valor_total() for p in producoes)
    print(f"\nReceita Total Prevista: {total:.2f}€")


menu()
