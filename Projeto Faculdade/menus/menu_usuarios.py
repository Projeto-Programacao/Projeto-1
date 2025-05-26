import json
import os

usuarios = []


def menu_usuarios():
    print("\n--- MENU USUÁRIOS ---")
    print("1. Criar usuário")
    print("2. Listar usuários")
    print("3. atualizar usuário")
    print("4. deletar usuário")
    print("0. Voltar")
    opc = input("escolha a opção que você deseja: ")
    if opc == '1':
        registrar_usuario()
    elif opc == '2':
        listar_usuario()
    elif opc == '3':
        login = input("Digite o login do usuário a ser atualizado: ")
        novo_nome = input("Novo nome (ou Enter para manter): ")
        nova_senha = input("Nova senha (ou Enter para manter): ")
        atualizar_usuario(login, novo_nome if novo_nome else None,
                          nova_senha if nova_senha else None)
    elif opc == '4':
        login = input("Digite o login do usuário a ser deletado: ")
        deletar_usuarios(login)
    elif opc == '0':
        print("Você saiu!")
    else:
        print("Opção inválida.")


def registrar_usuario():
    while True:
        nome = input("Nome: ").strip()
        if nome:
            break
        else:
            print("Prencha o espaço vazio!")

    while True:
        login = input("Login: ").strip()
        if login:
            break
        else:
            print("Prencha o espaço vazio!")

    if usuario_existente(login):
        print("ERRO. USUÁRIO EXISTENTE!")
        return

    while True:
        senha = input("Senha: ").strip()
        if senha:
            break
        else:
            print("Prencha o espaço vazio!")

    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print("ARQUIVO CORROMPIDO. CRIANDO NOVO")
                data = {"usuarios": []}
    else:
        data = {"usuarios": []}

    global usuarios
    usuarios = data["usuarios"]

    if not usuarios:
        novo_id = 1
    else:
        novo_id = usuarios[-1]["id"] + 1

    novo_usuario = {
        "id": novo_id,
        "nome": nome,
        "login": login,
        "senha": senha,
        "logado": False
    }

    usuarios.append(novo_usuario)
    data["usuarios"] = usuarios

    with open("usuarios.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Usuário registrado com sucesso!")


def listar_usuario():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                print("Erro. Arquivo corrompido ou vazio.")
                return
    else:
        print("Nenhum usuário encontrado.")
        return

    usuarios = dados.get("usuarios", [])

    if not usuarios:
        print("Lista de usuários vazia.")
        return

    print("=== LISTA DE USUÁRIOS REGISTRADOS ===")
    for usuario in usuarios:
        print(
            f"ID: {usuario['id']} | Nome: {usuario['nome']} | Login: {usuario['login']}")


def atualizar_usuario(login, novo_nome=None, nova_senha=None):
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as f:
            dados = json.load(f)
    else:
        print("Nenhum dado encontrado.")
        return

    atualizado = False
    for usuario in dados["usuarios"]:
        if usuario["login"] == login:
            if novo_nome:
                usuario["nome"] = novo_nome
            if nova_senha:
                usuario["senha"] = nova_senha
            atualizado = True
            break

    if atualizado:
        with open("usuarios.json", "w") as f:
            json.dump(dados, f, indent=4)
        print("Usuário atualizado com sucesso.")
    else:
        print("Usuário não encontrado.")


def deletar_usuarios(login):
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as f:
            dados = json.load(f)
    else:
        print("nenhum dado encontrado.")
        return
    usuarios = dados["usuarios"]
    novos_usuarios = [u for u in usuarios if u["login"] != login]

    if len(novos_usuarios) == len(usuarios):
        print("usuario não encontrado.")
        return
    with open("usuarios.json", "w") as f:
        json.dump({"usuarios": novos_usuarios}, f, indent=4)

    print("usuario deletado com sucesso")


def usuario_existente(login):
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as f:
            try:
                dados = json.load(f)
                for usuario in dados.get("usuarios", []):
                    if usuario["login"] == login:
                        return True
            except json.JSONDecodeError:
                return False
    return False
