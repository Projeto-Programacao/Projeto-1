import json
import os


def menu_denuncias():
    print("\n --- Menu de Denúncias --- ")
    print("1. Criar denúncia")
    print("2. Listar denúncias")
    print("3. Ler denúncias")
    print("4. Atualizar denúncia")
    print("5. Excluir denúncia")
    print("6. Encerrar programa")
    opcao = input("Escolha uma das opções:").strip()

    if opcao == "1":
        denuncia = input("Informe sua denúncia: ").strip()
        data_denuncia = input("Informe a data do ocorrido: ").strip()
        if not denuncia or not data_denuncia:
            print("Denúncia e data não podem estar vazias.")
        else:
            criar_denuncia(denuncia, data_denuncia)
    elif opcao == "2":
        listar_denuncias()
    elif opcao == "3":
        id_denuncia = int(
            input("Digite o ID da denúncia que deseja consultar:"))
        ler_denuncia_por_id(id_denuncia)
    elif opcao == "4":
        id_denuncia = int(input("ID da denúncia: "))
        nova_denuncia = input("Informe a nova denúncia: ").strip()
        nova_data = input("Informe a nova data do ocorrido: ").strip()
        if not nova_denuncia or not nova_data:
            print("Denúncia e data não podem estar vazias.")
        else:
            atualizar_denuncias(id_denuncia, nova_denuncia, nova_data)
    elif opcao == "5":
        id_denuncia = int(input("ID da denúncia a ser excluída: "))
        deletar_denuncia(id_denuncia)
    elif opcao == "6":
        print("Saiu!")
    else:
        print("Opção inválida.")


ARQUIVO = "denuncias.json"


def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r") as f:
        return json.load(f)


def salvar_dados(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f, indent=4)


def criar_denuncia(denuncia, data_denuncia):
    dados = carregar_dados()
    novo_id = 1 if not dados else dados[-1]['id'] + 1
    denuncia = {"id": novo_id, "denuncia": denuncia, "data": data_denuncia}
    dados.append(denuncia)
    salvar_dados(dados)
    print("Denúncia criada com sucesso!")


def listar_denuncias():
    dados = carregar_dados()
    for denuncia in dados:
        print(
            f"ID: {denuncia['id']} | Data: {denuncia['data']} | Denúncia: {denuncia['denuncia']}")


def ler_denuncia_por_id(id_denuncia):
    dados = carregar_dados()
    for denuncia in dados:
        if denuncia['id'] == id_denuncia:
            print("\n--- Detalhes da Denúncia ---")
            print(f"ID: {denuncia['id']}")
            print(f"Data: {denuncia['data']}")
            print(f"Denúncia: {denuncia['denuncia']}")
            return
    print("Denúncia não encontrada.")


def atualizar_denuncias(id_denuncia, nova_denuncia, nova_data):
    dados = carregar_dados()
    for denuncia in dados:
        if denuncia['id'] == id_denuncia:
            denuncia['denuncia'] = nova_denuncia
            denuncia['data'] = nova_data
            salvar_dados(dados)
            print("Denúncia atualizada com sucesso!")
            return
        print("Denúncia não encotrada.")


def deletar_denuncia(id_denuncia):
    dados = carregar_dados()
    dados = [denuncia for denuncia in dados if denuncia['id'] != id_denuncia]
    salvar_dados(dados)
    print("Denúncia deletada com sucesso!")