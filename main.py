'''

Nome:   Marlon Jhoni Lima Antonelo
Curso:  Raciocínio Computacional - Turma 03

'''

opcaoMenu = ["ESTUDANTES", "PROFESSORES", "DISCIPLINAS", "TURMAS", "MATRÍCULAS"]
opcaoMenuSecundario = ["INCLUIR", "LISTAR", "ATUALIZAR", "EXCLUIR"]
estudantes = []

while True:
    # Menu principal
    print("----- MENU PRINCIPAL -----\n\n"
    "(0) Gerenciar estudantes.\n"
    "(1) Gerenciar professores.\n"
    "(2) Gerenciar disciplinas.\n"
    "(3) Gerenciar turmas.\n"
    "(4) Gerenciar matrículas.\n"
    "(9) Sair.\n")

    try:
        #Coletar a opção escolhida pelo usuário
        opcao = int(input("Informe a opção desejada: "))
        
        if opcao == 0:
            print(f"Você escolheu a opção {opcaoMenu[opcao]}.\n")

            while True:
                #Menu secundário
                print(f"***** [{opcaoMenu[opcao]}] MENU DE OPERAÇÕES *****\n\n"
                "(0) Incluir.\n"
                "(1) Listar.\n"
                "(2) Atualizar.\n"
                "(3) Excluir.\n"
                "(9) Voltar ao menu principal.\n")

                try:
                    #Coletar a opção secundária escolhida pelo usuário
                    opcaoSecundaria = int(input("Informe a opção desejada: "))

                    #Incluir
                    if opcaoSecundaria == 0:
                        print(f"Você escolheu a opção secundária {opcaoMenuSecundario[opcaoSecundaria]}.\n")
                        print("===== INCLUSÃO =====")
                        codigo = int(input("Informe o código do estudante: "))
                        nome = input("Informe o nome do estudante: ")
                        cpf = int(input("Informe o CPF do estudante: "))

                        dados_estudantes = {
                            "cod_estudante": codigo,
                            "nome_estudante": nome,
                            "cpf_estudante": cpf
                        }

                        estudantes.append(dados_estudantes)
                        print("\nEstudante incluido\n")

                    #Listar
                    elif opcaoSecundaria == 1:
                        print(f"Você escolheu a opção secundária {opcaoMenuSecundario[opcaoSecundaria]}.\n")
                        if len(estudantes) ==  0: 
                            print("Não há estudantes cadastrados\n")
                        else:
                            print("===== LISTAGEM =====")
                            for estudante in estudantes:
                                print(estudante)
                            print("====================\n")

                    #Atualizar / Editar
                    elif opcaoSecundaria == 2:
                        print(f"Você escolheu a opção secundária {opcaoMenuSecundario[opcaoSecundaria]}.\n")
                        codigo_atualizar = int(input("Informe o código do estudante que deseja editar: "))
                        estudante_editado = None

                        for dicionario_estudantes in estudantes:
                            if dicionario_estudantes["cod_estudante"] == codigo_atualizar:
                                estudante_editado = dicionario_estudantes
                                break

                        if estudante_editado is None:
                            print(f"Codigo {codigo_atualizar} do estudante não encontrado, digite um código válido.")
                        else:
                            estudante_editado["cod_estudante"] = int(input("Digite o novo código do estudante: "))
                            estudante_editado["nome_estudante"] = input("Digite o novo nome do estudante: ")
                            estudante_editado["cpf_estudante"] = int(input("Digite o novo CPF do estudante: "))
                            print("\nEstudante atualizado.\n")

                    #Excluir
                    elif opcaoSecundaria == 3:
                        print(f"Você escolheu a opção secundária {opcaoMenuSecundario[opcaoSecundaria]}.\n")
                        codigo_excluir = int(input("Informe o código do estudante que deseja excluir: "))
                        estudante_removido = None

                        for dicionario_estudantes in estudantes:
                            if dicionario_estudantes["cod_estudante"] == codigo_excluir:
                                estudante_removido = dicionario_estudantes
                                break

                        #Digitou um código inválido
                        if estudante_removido is None:
                            print(f"Codigo {codigo_excluir} do estudante não encontrado, digite um código válido.")
                        else:
                            nome_estudante_removido = estudante_removido["nome_estudante"]
                            estudantes.remove(estudante_removido)
                            print(f"Estudante *{nome_estudante_removido}* excluido da lista.\n")
                    
                    elif opcaoSecundaria == 9:
                        print("Voltando ao menu principal.\n") 
                        break   

                    else:
                        print("Você digitou uma opção secundária *inválida*.\n")

                except ValueError:
                    print("Válido somente número inteiro")

        elif opcao >= 1 and opcao <= 4:
            print(f"Você escolheu a opção {opcaoMenu[opcao]}.\n"
                  "EM DESENVOLVIMENTO\n")

        elif opcao == 9:
            print("Você pediu para sair.")
            break

        else:
            print("Você digitou uma opção *inválida*.")
            
    except ValueError:
        print("Válido somente número inteiro")

print("===== ATUALIZAÇÃO =====")
print("Finalizando aplicação...")

