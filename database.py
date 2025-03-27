import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("DB_HOST")
database = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")


def conectar():
    try:
        conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None


def cadastrar_produto(nome, preco):
    """ Cadastra um novo produto """
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO produtos (nome, preco, ativo) VALUES (%s, %s, TRUE)", (nome, preco))
            conn.commit()
            print("✅ Produto cadastrado com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao cadastrar produto: {e}")
        finally:
            cursor.close()
            conn.close()


def inativar_produto(produto_id):
    """ Marca o produto como inativo em vez de excluí-lo """
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE produtos SET ativo = FALSE WHERE id = %s", (produto_id,))
            conn.commit()
            print("✅ Produto inativado com sucesso! Não poderá mais ser vendido.")
        except Exception as e:
            print(f"❌ Erro ao inativar produto: {e}")
        finally:
            cursor.close()
            conn.close()


def editar_produto(produto_id, novo_nome, novo_preco):
    """ Edita o nome e o preço de um produto existente """
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE produtos SET nome = %s, preco = %s WHERE id = %s",
                           (novo_nome, novo_preco, produto_id))
            conn.commit()
            print("✅ Produto editado com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao editar produto: {e}")
        finally:
            cursor.close()
            conn.close()


def registrar_pedido(produto_id, quantidade):
    """ Registra um novo pedido apenas se o produto estiver ativo """
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT preco, ativo FROM produtos WHERE id = %s", (produto_id,))
            produto = cursor.fetchone()
            if produto:
                preco, ativo = produto
                if not ativo:
                    print("❌ Este produto está inativo e não pode ser vendido!")
                    return
                valor_total = preco * quantidade
                cursor.execute("INSERT INTO pedidos (produto_id, quantidade, valor_total) VALUES (%s, %s, %s)",
                               (produto_id, quantidade, valor_total))
                conn.commit()
                print("✅ Pedido registrado com sucesso!")
            else:
                print("❌ Produto não encontrado!")
        except Exception as e:
            print(f"Erro ao registrar pedido: {e}")
        finally:
            cursor.close()
            conn.close()


def listar_pedidos():
    """ Lista todos os pedidos com os produtos associados """
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT p.id, pr.nome, p.quantidade, p.valor_total, p.data 
                FROM pedidos p 
                JOIN produtos pr ON p.produto_id = pr.id
            """)
            pedidos = cursor.fetchall()
            print("\n📜 Pedidos cadastrados:")
            for pedido in pedidos:
                print(
                    f"🆔 ID: {pedido[0]}, 🏷 Produto: {pedido[1]}, 📦 Quantidade: {pedido[2]}, 💰 Valor: R${pedido[3]}, 📅 Data: {pedido[4]}")
        except Exception as e:
            print(f"❌ Erro ao listar pedidos: {e}")
        finally:
            cursor.close()
            conn.close()
