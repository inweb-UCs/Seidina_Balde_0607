from programador import Programador
from designer import Designer

funcionarios = []

while True:
    print("\n1 - Adicionar programador")
    print("2 - Adicionar designer")
    print("3 - Listar funcionários")
    print("4 - Executar ações dos funcionários")
    print("0 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        salario = input("Salário: ")
        linguagem = input("Linguagem: ")
        p = Programador(nome, salario, linguagem)
        funcionarios.append(p)

    elif opcao == "2":
        nome = input("Nome: ")
        salario = input("Salário: ")
        ferramenta = input("Ferramenta: ")
        d = Designer(nome, salario, ferramenta)
        funcionarios.append(d)

    elif opcao == "3":
        for f in funcionarios:
            f.mostrar_info()
            print("-----")

    elif opcao == "4":
        for f in funcionarios:
            f.acao()

    elif opcao == "0":
        break

    else:
        print("Opção inválida")