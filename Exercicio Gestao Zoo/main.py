from mamifero import Mamifero
from ave import Ave

animais = []

while True:
    print("\n1 - Registar mamífero")
    print("2 - Registar ave")
    print("3 - Listar animais")
    print("4 - Ficha médica do animal")
    print("5 - Registar consultas efetuadas")
    print("0 - Sair")

    opcao = input("Opção: ")

    # 1 - Registar mamífero
    if opcao == "1":
        nome = input("Nome: ")
        idade = input("Idade: ")
        especie = input("Espécie: ")
        alimentacao = input("Tipo de alimentação: ")

        m = Mamifero(nome, idade, especie, alimentacao)
        animais.append(m)

    # 2 - Registar ave
    elif opcao == "2":
        nome = input("Nome: ")
        idade = input("Idade: ")
        especie = input("Espécie: ")
        envergadura = input("Envergadura das asas: ")

        a = Ave(nome, idade, especie, envergadura)
        animais.append(a)

    # 3 - Listar animais
    elif opcao == "3":
        for a in animais:
            a.mostrar_info()
            print("-----")

    # 4 - Ficha médica
    elif opcao == "4":
        nome = input("Nome do animal: ")
        encontrado = False

        for a in animais:
            if a.nome == nome:
                a.mostrar_ficha_medica()
                encontrado = True

        if not encontrado:
            print("Animal não encontrado.")

    # 5 - Registar consulta
    elif opcao == "5":
        nome = input("Nome do animal: ")
        encontrado = False

        for a in animais:
            if a.nome == nome:
                data = input("Data da consulta: ")
                descricao = input("Descrição: ")
                observacoes = input("Observações: ")

                consulta = f"{data} - {descricao} - {observacoes}"
                a.registar_consulta(consulta)

                encontrado = True

        if not encontrado:
            print("Animal não encontrado.")

    elif opcao == "0":
        break

    else:
        print("Opção inválida.")