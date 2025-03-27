from database import (
    cadastrar_produto, inativar_produto, editar_produto,
    registrar_pedido, listar_pedidos, cancelar_pedido
)


def menu_principal():
    """ Menu principal do sistema """
    while True:
        print("\n========= 🍞 Padaria System =========")
        print("1️⃣ Cadastrar Produto")
        print("2️⃣ Gerenciar Pedidos")
        print("3️⃣ Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            menu_cadastrar_produto()
        elif opcao == '2':
            menu_gerenciar_pedido()
        elif opcao == '3':
            print("👋 Saindo do sistema...")
            break
        else:
            print("❌ Opção inválida!")


def menu_cadastrar_produto():
    """ Submenu para gerenciar produtos """
    while True:
        print("\n========= 📦 Gerenciamento de Produtos =========")
        print("1️⃣ Cadastrar Produto")
        print("2️⃣ Inativar Produto")
        print("3️⃣ Editar Produto")
        print("4️⃣ Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            cadastrar_produto(nome, preco)

        elif opcao == '2':
            produto_id = int(input("ID do produto que deseja inativar: "))
            inativar_produto(produto_id)

        elif opcao == '3':
            produto_id = int(input("ID do produto que deseja editar: "))
            novo_nome = input("Novo nome: ")
            novo_preco = float(input("Novo preço: "))
            editar_produto(produto_id, novo_nome, novo_preco)

        elif opcao == '4':
            break

        else:
            print("❌ Opção inválida!")


def menu_gerenciar_pedido():
    """ Submenu para gerenciar pedidos """
    while True:
        print("\n========= 🛒 Gerenciamento de Pedidos =========")
        print("1️⃣ Registrar Pedido")
        print("2️⃣ Cancelar Pedido")
        print("3️⃣ Listar Pedidos")
        print("4️⃣ Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            produto_id = int(input("ID do produto: "))
            quantidade = int(input("Quantidade: "))
            registrar_pedido(produto_id, quantidade)

        elif opcao == '2':
            pedido_id = int(input("ID do pedido que deseja cancelar: "))
            cancelar_pedido(pedido_id)

        elif opcao == '3':
            listar_pedidos()

        elif opcao == '4':
            break
        else:
            print("❌ Opção inválida!")


if __name__ == "__main__":
    menu_principal()


