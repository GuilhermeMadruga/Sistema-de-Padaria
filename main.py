from database import cadastrar_produto, registrar_pedido, listar_pedidos

def menu():
    while True:
        print("\n========= Padaria System =========")
        print("1. Cadastrar Produto")
        print("2. Registrar Pedido")
        print("3. Listar Pedidos")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            cadastrar_produto(nome, preco)

        elif opcao == '2':
            produto_id = int(input("ID do produto: "))
            quantidade = int(input("Quantidade: "))
            registrar_pedido(produto_id, quantidade)

        elif opcao == '3':
            listar_pedidos()

        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()