import json
from filelock import FileLock
from pathlib import Path
from menus.denuncias import menu_denuncias
from menus.menu_usuarios import menu_usuarios
# from menus.menu_evidencias import menu_evidencias


def load_json(filepath):
    path = Path(filepath)
    lock_path = f"{filepath}.lock"
    with FileLock(lock_path):
        if not path.exists():
            return {}
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)


def save_json(filepath, data):
    lock_path = f"{filepath}.lock"
    with FileLock(lock_path):
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


def exibir_menu_principal():
    print("\n--- MENU PRINCIPAL ---")
    print("1. Denúncias")
    print("2. Evidências")
    print("3. Usuários")
    print("4. Sair")
    return input("Escolha uma opção: ")


if __name__ == "__main__":
    while True:
        escolha = exibir_menu_principal()

        if escolha == "1":
            menu_denuncias()
        elif escolha == "2":
            # menu_evidencias()  # descomentar quando criar
            print("Menu de evidências ainda não implementado.")
        elif escolha == "3":
            menu_usuarios()
        elif escolha == "4":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")
