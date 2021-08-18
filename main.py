def existe_contato(lista, nome):
    if len(lista) > 0:
        for contato in lista:
            if contato['nome'] == nome:
                return True

        return False


def inserir(lista):
    while True:
        nome = input("Digite o Nome do contato: ")

        if not existe_contato(lista, nome):
            break

        else:
            print("Esse nome já foi cadastrado. ")
            print("Por favor, tente outro nome.")

    contato = {
        "nome": nome,"email": input("Digite seu e-mail "), "tel": input("Digite seu telefone"),"twitter": input("Digite seu Twitter"),
        "instagram": input("Digite seu Instagram")
    }

    lista.append(contato)

    print("O contato {} foi cadastrado com sucesso!\n".format(contato["nome"]))


def pesquisar(lista):
    print("Pesquisar Contato")
    if len(lista) > 0:
        nome = input("Digite o nome do contato a ser Pesquisado: ")
        if existe_contato(lista, nome):
            print("O contato foi encontrado. As informações seguem abaixo")
            for contato in lista:
                if contato["nome"] == nome:
                    print("Nome: {} ".format(contato["nome"]))
                    print("Email: {} ".format(contato["email"]))
                    print("Telefone: {} ".format(contato["tel"]))
                    print("Twitter: {} ".format(contato["twitter"]))
                    print("Instagram: {} ".format(contato["instagram"]))
                    print("===============================================\n")
                    break

        else:
            print("Não existe contato cadastrado no sistema esse nome{}. \n".format(nome))
    else:
        print("Não existe nenhum contato cadastrado no sistema.\n")


def alterar(lista):
    print("Alterar Contato")
    if len(lista) > 0:
        nome = input("Digite o nome do contato a ser Alterado: ")
        if existe_contato(lista, nome):
            print("O contato foi encontrado. As informações seguem abaixo")
            for contato in lista:
                if contato["nome"] == nome:
                    print("Nome: {} ".format(contato["nome"]))
                    print("Email: {} ".format(contato["email"]))
                    print("Telefone: {} ".format(contato["tel"]))
                    print("Twitter: {} ".format(contato["twitter"]))
                    print("Instagram: {} ".format(contato["instagram"]))
                    print("===============================================\n")

                    contato["nome"] = input("Digite o novo nome do contato:")
                    contato["email"] = input("Digite o novo Email do contato:")
                    contato["tel"] = input("Digite o novo Telefone do contato:")
                    contato["twitter"] = input("Digite o novo Twitter do contato:")
                    contato["instagram"] = input("Digite o novo Instagram do contato:")
                    print("Os dados do contato {} foram alterados com sucesso!.\n".format(nome))
                    break


            else:
                print("Não existe contato cadastrado no sistema esse nome{}. \n".format(nome))
        else:
            print("Não existe nenhum contato cadastrado no sistema.\n")


def remover(lista):
    print("Excluir Contato")
    if len(lista) > 0:
        nome = input("Digite o nome do contato a ser excluído: ")
        if existe_contato(lista, nome):
            print("O contato foi encontrado. As informações seguem abaixo")
            for i, contato in enumerate(lista):
                if contato["nome"] == nome:
                    print("Nome: {} ".format(contato["nome"]))
                    print("Email: {} ".format(contato["email"]))
                    print("Telefone: {} ".format(contato["tel"]))
                    print("Twitter: {} ".format(contato["twitter"]))
                    print("Instagram: {} ".format(contato["instagram"]))
                    print("===============================================\n")

                    del lista[i]

                    print("O contato foi apagado com sucesso")
                    break

                else:
                    print("Não existe contato cadastrado no sistema esse nome{}. \n".format(nome))
        else:
            print("Não existe nenhum contato cadastrado no sistema.\n")

def relatorio(lista):
    print("== Relatório da Agenda Telefônica ==")
    if len(lista) > 0:
        for i, contato in enumerate (lista):
            print("Contato {}:". format(i+1))
            print("\tNome: {} ".format(contato["nome"]))
            print("\tEmail: {} ".format(contato["email"]))
            print("\tTelefone: {} ".format(contato["tel"]))
            print("\tTwitter: {} ".format(contato["twitter"]))
            print("\tInstagram: {} ".format(contato["instagram"]))
            print("==================================================")

        print ("Quantidade de contatos: {}\n".format(len(lista)))
    else:
        print("Não existe nenhum contato cadastrado na agenda\n")



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
        print("5 - Gerar Relatório")
        print("6 - Sair")
        opção = int(input("> "))

        if opção == 1:
            inserir(lista)

        elif opção == 2:
            pesquisar(lista)

        elif opção == 3:
            alterar(lista)

        elif opção == 4:
            remover(lista)

        elif opção == 5:
            relatorio(lista)

        elif opção == 6:
            print("Saindo da Lista Telefônica....")
            break
        else:
            print("Opção Inválida")


principal()