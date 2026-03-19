from database import create_table, create_user, get_users


def menu():
    while True:
        print("1- Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Sair")

        opcao = input("Digite sua opção: ")

        if opcao == "1":
            nome = input("Digite seu nome: ")
            email = input("Digite seu email: ")
            create_user(nome,email)
        
        elif opcao == "2":
            users = get_users()
            for user in users:
                print(f"{user[0]} - {user[1]} - {user[2]}")

        elif opcao == "3":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    create_table()
    menu()
