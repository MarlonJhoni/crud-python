'''

Nome:     Marlon Jhoni Lima Antonelo
Curso:    Análise e Desenvolvimento de Sistemas  
Matéria:  Raciocínio Computacional - Turma 03

'''

def menu_principal():
    print("----- MENU PRINCIPAL -----\n\n"
    "(0) Gerenciar estudantes.\n"
    "(1) Gerenciar professores.\n"
    "(2) Gerenciar disciplinas.\n"
    "(3) Gerenciar turmas.\n"
    "(4) Gerenciar matrículas.\n"
    "(9) Sair.\n")

    return int(input("Informe a opção desejada: "))
       
def menu_operacao():
    print("(0) Cadastrar.\n"
    "(1) Listar.\n"
    "(2) Atualizar.\n"
    "(3) Excluir.\n"
    "(9) Voltar ao menu principal.\n")

    return int(input("Informe a opção desejada: "))

def cadastrar_estudante(estudantes):
    print("===== INCLUSÃO =====")
    codigo = int(input("Informe o código do estudante: "))
    nome = input("Informe o nome do estudante: ")
    cpf = input("Informe o CPF do estudante: ")

    dados_estudantes = {
        "cod_estudante": codigo,
        "nome_estudante": nome,
        "cpf_estudante": cpf
    }

    estudantes.append(dados_estudantes)
    print("\nEstudante incluido\n")

def verificar_cadastro_estudantes(estudantes):
    if len(estudantes) > 0:
        return True
    else:
        print("Não há estudantes cadastrados.\n")

def listar_estudades(estudantes):
    if verificar_cadastro_estudantes(estudantes):
        print("===== LISTAGEM =====")
        for estudante in estudantes:
            print(estudante)
        print("====================\n")

def editar_estudante(estudantes):
    if verificar_cadastro_estudantes(estudantes):
        codigo_atualizar = int(input("Informe o código do estudante que deseja editar: "))
        estudante_editado = None

        for dicionario_estudantes in estudantes:
            if dicionario_estudantes["cod_estudante"] == codigo_atualizar:
                estudante_editado = dicionario_estudantes
                break

        if estudante_editado is None:
            print(f"Codigo {codigo_atualizar} do estudante não encontrado, digite um código válido.\n")
        else:
            estudante_editado["cod_estudante"] = int(input("Digite o novo código do estudante: "))
            estudante_editado["nome_estudante"] = input("Digite o novo nome do estudante: ")
            estudante_editado["cpf_estudante"] = input("Digite o novo CPF do estudante: ")
            print("\nEstudante atualizado.\n")
    
def excluir_estudante(estudantes):
    if verificar_cadastro_estudantes(estudantes):
        codigo_excluir = int(input("Informe o código do estudante que deseja excluir: "))
        estudante_removido = None

        for dicionario_estudantes in estudantes:
            if dicionario_estudantes["cod_estudante"] == codigo_excluir:
                estudante_removido = dicionario_estudantes
                break

        #Digitou um código inválido
        if estudante_removido is None:
            print(f"Codigo {codigo_excluir} do estudante não encontrado, digite um código válido.\n")
        else:
            nome_estudante_removido = estudante_removido["nome_estudante"]
            estudantes.remove(estudante_removido)
            print(f"Estudante *{nome_estudante_removido}* excluido da lista.\n")



opcao_menu_principal = ["ESTUDANTES", "PROFESSORES", "DISCIPLINAS", "TURMAS", "MATRÍCULAS"]
opcao_menu_operacao = ["CADASTRAR", "LISTAR", "ATUALIZAR", "EXCLUIR"]
estudantes = []

while True:
    try:
        # Menu principal
        opcao = menu_principal()
            
        #Menu de opreações
        if opcao == 0:
            print(f"Você escolheu a opção {opcao_menu_principal[opcao]}.\n")
            while True:
                try:
                    #Coletar a opção do menu de operações escolhida pelo usuário
                    print(f"***** [{opcao_menu_principal[opcao]}] MENU DE OPERAÇÕES *****\n")
                    opcao_secundaria = menu_operacao()

                    #Cadastrar Novo Estudante
                    if opcao_secundaria == 0:
                        print(f"Você escolheu a opção secundária {opcao_menu_operacao[opcao_secundaria]}.\n")
                        cadastrar_estudante(estudantes)

                    #Listar
                    elif opcao_secundaria == 1:
                        print(f"Você escolheu a opção secundária {opcao_menu_operacao[opcao_secundaria]}.\n")
                        listar_estudades(estudantes)

                    #Atualizar / Editar
                    elif opcao_secundaria == 2:
                        print(f"Você escolheu a opção secundária {opcao_menu_operacao[opcao_secundaria]}.\n")
                        editar_estudante(estudantes)

                    #Excluir
                    elif opcao_secundaria == 3:
                        print(f"Você escolheu a opção secundária {opcao_menu_operacao[opcao_secundaria]}.\n")
                        excluir_estudante(estudantes)
                    
                    elif opcao_secundaria == 9:
                        print("Voltando ao menu principal.\n") 
                        break   

                    else:
                        print("Você digitou uma opção secundária *inválida*.\n")

                except ValueError:
                    print("Válido somente número inteiro\n")

        elif opcao >= 1 and opcao <= 4:
            print(f"Você escolheu a opção {opcao_menu_principal[opcao]}.\n"
                    "EM DESENVOLVIMENTO\n")

        elif opcao == 9:
            print("Você pediu para sair.")
            break

        else:
            print("Você digitou uma opção *inválida*.\n")
            
    except ValueError:
        print("Válido somente número inteiro\n")


print("===== ATUALIZAÇÃO =====")
print("Finalizando aplicação...")

