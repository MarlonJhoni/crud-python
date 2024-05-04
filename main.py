'''

Nome:     Marlon Jhoni Lima Antonelo
Curso:    Análise e Desenvolvimento de Sistemas  
Matéria:  Raciocínio Computacional - Turma 03

'''
import json

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

def cadastrar_estudante_ou_professor(nome_arquivo):
    print("===== INCLUSÃO =====")
    codigo1 = int(input("Informe o código: "))
    nome = input("Informe o nome: ")
    cpf = input("Informe o CPF: ")

    dados_cadastro = {
        "Código": codigo1,
        "Nome": nome,
        "CPF": cpf
    }

    lista = ler_dados(nome_arquivo)

    if vericar_codigo(lista, codigo1):
       return

    lista.append(dados_cadastro)
    print("\nCadastro incluido\n")
    salvar_dados(lista,nome_arquivo)

def cadastrar_disciplina(nome_arquivo):
    print("===== INCLUSÃO =====")
    codigo1 = int(input("Informe o código da disciplina: "))
    nome = input("Informe o nome da disciplina: ")

    dados_cadastro = {
        "Código": codigo1,
        "Nome": nome,
    }

    lista = ler_dados(nome_arquivo)

    if vericar_codigo(lista, codigo1):
       return

    lista.append(dados_cadastro)
    print("\nCadastro incluido\n")
    salvar_dados(lista,nome_arquivo)

def cadastrar_turma(nome_arquivo):
    print("===== INCLUSÃO =====")
    codigo1 = int(input("Informe o código da turma: "))
    codigo2 = int(input("Informe o código do professor: "))
    codigo3 = int(input("Informe o código do estudante: "))

    lista = ler_dados(nome_arquivo)

    if vericar_codigo(lista, codigo1):
       return

    dados_cadastro = {
        "Código": codigo1,
        "Código do Professor": codigo2,
        "Código do Estudante": codigo3,
    }

    lista.append(dados_cadastro)
    print("\nCadastro incluido\n")
    salvar_dados(lista,nome_arquivo)

def cadastrar_matricula(nome_arquivo):
    print("===== INCLUSÃO =====")
    codigo1 = int(input("Informe o código da turma: "))
    codigo2 = int(input("Informe o código do estudante: "))

    lista = ler_dados(nome_arquivo)
    if vericar_codigo(lista, codigo1):
       return

    dados_cadastro = {
        "Código": codigo1,
        "Código do Estudante": codigo2,
    }

    lista.append(dados_cadastro)
    print("\nCadastro incluido\n")
    salvar_dados(lista,nome_arquivo)

def vericar_codigo(lista,codigo):
    for i in lista:
        if i["Código"] == codigo:
            print(f"\nCódigo já existente.\n")
            return True
    return False

def verificar_cadastro(lista_dados):
    if len(lista_dados) > 0:
        return True
    else:
        print("Não há dados cadastrados.\n")
        return False

def listar_cadastro(nome_arquivo):
    lista_dados = ler_dados(nome_arquivo)
    if verificar_cadastro(lista_dados):
        print("===== LISTAGEM =====")
        for i in lista_dados:
            print(i)
        print("====================\n")

def editar_cadastro(nome_arquivo):
    lista_dados = ler_dados(nome_arquivo)    
    if verificar_cadastro(lista_dados):
        codigo_atualizar = int(input("Informe o código que deseja editar: "))
        cadastro_editado = None

        for i in lista_dados:
            if i["Código"] == codigo_atualizar:
                cadastro_editado = i
                break

        if cadastro_editado is None:
            print(f"Codigo {codigo_atualizar} não encontrado, digite um código válido.\n")
        else:
            cadastro_editado["Código"] = int(input("Digite o novo código: "))
            cadastro_editado["Nome"] = input("Digite o novo nome: ")
            cadastro_editado["CPF"] = input("Digite o novo CPF: ")
            print("\nCadastro atualizado.\n")
            salvar_dados(lista_dados,nome_arquivo)

def editar_disciplina(nome_arquivo):
    lista_dados = ler_dados(nome_arquivo)    
    if verificar_cadastro(lista_dados):
        codigo_atualizar = int(input("Informe o código que deseja editar: "))
        cadastro_editado = None

        for i in lista_dados:
            if i["Código"] == codigo_atualizar:
                cadastro_editado = i
                break

        if cadastro_editado is None:
            print(f"Codigo {codigo_atualizar} não encontrado, digite um código válido.\n")
        else:
            cadastro_editado["Código"] = int(input("Digite o novo código: "))
            cadastro_editado["Nome"] = input("Digite o novo nome da disciplina: ")
            print("\nCadastro atualizado.\n")
            salvar_dados(lista_dados,nome_arquivo)

def editar_turma(nome_arquivo):
    lista_dados = ler_dados(nome_arquivo)    
    if verificar_cadastro(lista_dados):
        codigo_atualizar = int(input("Informe o código que deseja editar: "))
        cadastro_editado = None

        for i in lista_dados:
            if i["Código"] == codigo_atualizar:
                cadastro_editado = i
                break

        if cadastro_editado is None:
            print(f"Codigo {codigo_atualizar} não encontrado, digite um código válido.\n")
        else:
            cadastro_editado["Código"] = int(input("Digite o novo código: "))
            cadastro_editado["Código do Professor"] = input("Digite o novo nome do professor: ")
            cadastro_editado["Código do Estudante"] = input("Digite o novo nome do estudante: ")
            print("\nCadastro atualizado.\n")
            salvar_dados(lista_dados,nome_arquivo)

def editar_matricula(nome_arquivo):
    lista_dados = ler_dados(nome_arquivo)    
    if verificar_cadastro(lista_dados):
        codigo_atualizar = int(input("Informe o código que deseja editar: "))
        cadastro_editado = None

        for i in lista_dados:
            if i["Código"] == codigo_atualizar:
                cadastro_editado = i
                break

        if cadastro_editado is None:
            print(f"Codigo {codigo_atualizar} não encontrado, digite um código válido.\n")
        else:
            cadastro_editado["Código"] = int(input("Digite o novo código: "))
            cadastro_editado["Código do Estudante"] = input("Digite o novo nome do estudante: ")
            print("\nCadastro atualizado.\n")
            salvar_dados(lista_dados,nome_arquivo)


def excluir_cadastro(nome_arquivo):
    lista_dados = ler_dados(nome_arquivo)
    if verificar_cadastro(lista_dados):
        codigo_excluir = int(input("Informe o código que deseja excluir: "))
        cadastro_removido = None

        for i in lista_dados:
            if i["Código"] == codigo_excluir:
                cadastro_removido = i
                break

        #Digitou um código inválido
        if cadastro_removido is None:
            print(f"Codigo {codigo_excluir} do cadstro não encontrado, digite um código válido.\n")
        else:
            lista_dados.remove(cadastro_removido)
            print(f"Cadastro excluido da lista.\n")
            salvar_dados(lista_dados,nome_arquivo)


def salvar_dados(lista, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False)


def ler_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8' ) as arquivo:
            lista = json.load(arquivo)
        
        return lista
    except:
        return []
    
def processar_menu_operacoes(opcao_secundaria,nome_arquivo,titulo,opcao_primaria):
    #Cadastrar Novo
    if opcao_secundaria == 0:
        print(f"Você escolheu a opção secundária {titulo[opcao_secundaria]}.\n")
        if opcao_primaria == 0 or opcao_primaria == 1:
            cadastrar_estudante_ou_professor(nome_arquivo)
        elif opcao_primaria == 2:
            cadastrar_disciplina(nome_arquivo)
        elif opcao_primaria == 3:
            cadastrar_turma(nome_arquivo)
        elif opcao_primaria == 4:
            cadastrar_matricula(nome_arquivo)
    

    #Listar
    elif opcao_secundaria == 1:
        print(f"Você escolheu a opção secundária {titulo[opcao_secundaria]}.\n")
        listar_cadastro(nome_arquivo)

    #Atualizar / Editar
    elif opcao_secundaria == 2:
        print(f"Você escolheu a opção secundária {titulo[opcao_secundaria]}.\n")
        if opcao_primaria == 0 or opcao_primaria == 1:
            editar_cadastro(nome_arquivo)
        elif opcao_primaria == 2:
            editar_disciplina(nome_arquivo)
        elif opcao_primaria == 3:
            editar_turma(nome_arquivo)
        elif opcao_primaria == 4:
            editar_matricula(nome_arquivo)

    #Excluir
    elif opcao_secundaria == 3:
        print(f"Você escolheu a opção secundária {titulo[opcao_secundaria]}.\n")
        excluir_cadastro(nome_arquivo)
    
    elif opcao_secundaria == 9:
        print("Voltando ao menu principal.\n") 
        return False

    else:
        print("Você digitou uma opção secundária *inválida*.\n")

    return True


titulo_menu_principal = ["ESTUDANTES", "PROFESSORES", "DISCIPLINAS", "TURMAS", "MATRÍCULAS"]
titulo_menu_operacao = ["CADASTRAR", "LISTAR", "ATUALIZAR", "EXCLUIR"]

arquivo_estudante = "dados/estudantes.json"
arquivo_professor = "dados/professores.json"
arquivo_disciplina = "dados/disciplinas.json"
arquivo_turma = "dados/turmas.json"
arquivo_matricula = "dados/matriculas.json"


while True:
    try:
        # Menu principal
        opcao = menu_principal()

        if opcao == 0:
            print(f"Você escolheu a opção {titulo_menu_principal[opcao]}.\n")
            while True:
                try:
                    #Coletar a opção do menu de operações escolhida pelo usuário
                    print(f"***** [{titulo_menu_principal[opcao]}] MENU DE OPERAÇÕES *****\n")
                    opcao_secundaria = menu_operacao()
                    if not processar_menu_operacoes(opcao_secundaria,arquivo_estudante,titulo_menu_operacao,opcao):
                        break
                except ValueError:
                    print("Válido somente número inteiro\n")

        elif opcao == 1:
            print(f"Você escolheu a opção {titulo_menu_principal[opcao]}.\n")
            while True:
                try:
                    #Coletar a opção do menu de operações escolhida pelo usuário
                    print(f"***** [{titulo_menu_principal[opcao]}] MENU DE OPERAÇÕES *****\n")
                    opcao_secundaria = menu_operacao()
                    if not processar_menu_operacoes(opcao_secundaria,arquivo_professor,titulo_menu_operacao,opcao):
                        break
                except ValueError:
                    print("Válido somente número inteiro\n")

        elif opcao == 2:
            print(f"Você escolheu a opção {titulo_menu_principal[opcao]}.\n")
            while True:
                try:
                    #Coletar a opção do menu de operações escolhida pelo usuário
                    print(f"***** [{titulo_menu_principal[opcao]}] MENU DE OPERAÇÕES *****\n")
                    opcao_secundaria = menu_operacao()
                    if not processar_menu_operacoes(opcao_secundaria,arquivo_disciplina,titulo_menu_operacao,opcao):
                        break
                except ValueError:
                    print("Válido somente número inteiro\n")

        elif opcao == 3:
            print(f"Você escolheu a opção {titulo_menu_principal[opcao]}.\n")
            while True:
                try:
                    #Coletar a opção do menu de operações escolhida pelo usuário
                    print(f"***** [{titulo_menu_principal[opcao]}] MENU DE OPERAÇÕES *****\n")
                    opcao_secundaria = menu_operacao()
                    if not processar_menu_operacoes(opcao_secundaria,arquivo_turma,titulo_menu_operacao,opcao):
                        break
                except ValueError:
                    print("Válido somente número inteiro\n")

        elif opcao == 4:
            print(f"Você escolheu a opção {titulo_menu_principal[opcao]}.\n")
            while True:
                try:
                    #Coletar a opção do menu de operações escolhida pelo usuário
                    print(f"***** [{titulo_menu_principal[opcao]}] MENU DE OPERAÇÕES *****\n")
                    opcao_secundaria = menu_operacao()
                    if not processar_menu_operacoes(opcao_secundaria,arquivo_matricula,titulo_menu_operacao,opcao):
                        break
                except ValueError:
                    print("Válido somente número inteiro\n")

        elif opcao == 9:
            print("Você pediu para sair.")
            break

        else:
            print("Você digitou uma opção *inválida*.\n")
            
    except ValueError:
        print("Válido somente número inteiro\n")


print("===== ATUALIZAÇÃO =====")
print("Finalizando aplicação...")