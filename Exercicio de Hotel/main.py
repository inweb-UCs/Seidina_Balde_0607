from cliente import Cliente
from quarto import Quarto
from reserva import Reserva

clientes = []
quartos = []
reservas = []
id_reserva_atual = 1

def procurar_cliente(id_cliente):
    for c in clientes:
        if c.get_id() == id_cliente:
            return c
    return None

def procurar_quarto(numero):
    for q in quartos:
        if q.get_numero() == numero:
            return q
    return None

def procurar_reserva(id_reserva):
    for r in reservas:
        if r.get_id() == id_reserva:
            return r
    return None

while True:
    print("\n--- MENU HOTEL ---")
    print("1 - Registar Cliente")
    print("2 - Registar Quarto")
    print("3 - Criar Reserva")
    print("4 - Listar Clientes")
    print("5 - Listar Quartos")
    print("6 - Listar Reservas")
    print("7 - Informação de Cliente")
    print("8 - Informação de Quarto")
    print("9 - Cancelar Reserva")
    print("0 - Sair")

    op = input("Opção: ")

    if op == "1":
        idc = input("ID do cliente: ")
        nome = input("Nome: ")
        email = input("Email: ")
        clientes.append(Cliente(idc, nome, email))
        print("Cliente registado.")

    elif op == "2":
        num = input("Número do quarto: ")
        preco = float(input("Preço por noite: "))
        quartos.append(Quarto(num, preco))
        print("Quarto registado.")

    elif op == "3":
        idc = input("ID do cliente: ")
        cliente = procurar_cliente(idc)
        if cliente is None:
            print("Cliente não encontrado.")
            continue

        num = input("Número do quarto: ")
        quarto = procurar_quarto(num)
        if quarto is None:
            print("Quarto não encontrado.")
            continue

        if quarto.is_ocupado():
            print("Quarto ocupado.")
            continue

        noites = int(input("Número de noites: "))
        reserva = Reserva(id_reserva_atual, cliente, quarto, noites)
        reservas.append(reserva)
        quarto.set_ocupado(True)
        id_reserva_atual += 1
        print("Reserva criada.")

    elif op == "4":
        for c in clientes:
            print(c.info())

    elif op == "5":
        for q in quartos:
            print(q.info())

    elif op == "6":
        for r in reservas:
            print(r.info())

    elif op == "7":
        idc = input("ID do cliente: ")
        cliente = procurar_cliente(idc)
        if cliente is None:
            print("Cliente não encontrado.")
        else:
            print(cliente.info())
            print("Reservas:")
            for r in reservas:
                if r.get_cliente().get_id() == idc:
                    print(r.info())

    elif op == "8":
        num = input("Número do quarto: ")
        quarto = procurar_quarto(num)
        if quarto is None:
            print("Quarto não encontrado.")
        else:
            print(quarto.info())
            for r in reservas:
                if r.get_quarto().get_numero() == num and r.is_ativa():
                    print("Reserva associada:")
                    print(r.info())

    elif op == "9":
        rid = int(input("ID da reserva: "))
        reserva = procurar_reserva(rid)
        if reserva is None:
            print("Reserva não encontrada.")
        else:
            reserva.cancelar()
            print("Reserva cancelada.")

    elif op == "0":
        break

    else:
        print("Opção inválida.")