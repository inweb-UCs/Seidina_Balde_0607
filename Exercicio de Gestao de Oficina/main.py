from proprietario import Proprietario
from veiculo import Veiculo
from peca import Peca
from intervencao import Intervencao

proprietarios = []
veiculos = []
pecas = []
intervencoes = []

while True:
    print("\n1 - Registar proprietário")
    print("2 - Registar veículo")
    print("3 - Registar peça")
    print("4 - Registar intervenção")
    print("5 - Consultar intervenções por matrícula")
    print("0 - Sair")

    opcao = input("Opção: ")

    # 1 - Registar proprietário
    if opcao == "1":
        nif = input("NIF: ")
        nome = input("Nome: ")
        morada = input("Morada: ")

        p = Proprietario(nif, nome, morada)
        proprietarios.append(p)

    # 2 - Registar veículo
    elif opcao == "2":
        nif = input("NIF do proprietário: ")

        dono = None
        for p in proprietarios:
            if p.nif == nif:
                dono = p

        if dono is None:
            print("Proprietário não encontrado.")
        else:
            matricula = input("Matrícula: ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")

            v = Veiculo(dono, matricula, marca, modelo)
            veiculos.append(v)

    # 3 - Registar peça
    elif opcao == "3":
        ref = input("Referência: ")
        desc = input("Descrição: ")

        pc = Peca(ref, desc)
        pecas.append(pc)

    # 4 - Registar intervenção
    elif opcao == "4":
        mat = input("Matrícula do veículo: ")

        veic = None
        for v in veiculos:
            if v.matricula == mat:
                veic = v

        if veic is None:
            print("Veículo não encontrado.")
        else:
            data = input("Data da intervenção: ")
            inter = Intervencao(veic, data)

            print("Peças disponíveis:")
            for p in pecas:
                print(p.referencia, "-", p.descricao)

            while True:
                ref = input("Referência da peça (0 para terminar): ")
                if ref == "0":
                    break

                for p in pecas:
                    if p.referencia == ref:
                        inter.adicionar_peca(p)

            intervencoes.append(inter)

    # 5 - Consultar intervenções por matrícula
    elif opcao == "5":
        mat = input("Matrícula: ")

        encontrou = False
        for i in intervencoes:
            if i.veiculo.matricula == mat:
                i.mostrar()
                encontrou = True

        if not encontrou:
            print("Nenhuma intervenção encontrada.")

    elif opcao == "0":
        break

    else:
        print("Opção inválida.")