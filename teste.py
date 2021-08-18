def adcionar(lista):
    while true:
        email = input("Digite o e-mail do contato: ")
        if not existe_contato(email):
            break
        else:
            print("Esse e-mail já foi cadastrado. ")
            print("Por favor, tente outro e-mail.")

    contato = {
        "email": email,
        "nome": input("Digite seu nome "),
        "tel": input("Digite seu telefone")
    }

    lista.append(Contato)

    print("O contato {} foi cadastrado com sucesso!\n".format(contato["nome"]))


def pesquisar():
    pass


def alterar():
    pass


def remover():
    pass


def sair():
    pass


def principal():
    lista = []
    while True:
        print("------------------------------------")
        print("---------AGENDA DE TELEFÔNICA-------")
        print("------------------------------------")
        print("1 - Inserir um novo Contato")
        print("2 - Consultar Contato ")
        print("3 - Alterar Contato")
        print("4 - Remover Contato")
        print("5 - Sair")
        opção = int(input(">"))

        if opção == 1:
            adicionar(lista)

        elif opção == 2:
            pesquisar()

        elif Opção == 3:
            alterar()

        elif Opção == 4:
            remover()

        elif Opção == 5:
            print("Saindo da Lista Telefônica....")
            break
        else:
            print("Opção Inválida")


principal()


