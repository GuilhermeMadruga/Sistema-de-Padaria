import psycopg2
import os
from dotenv import load_dotenv
from datetime import datetime

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
    """ Registra um novo pedido apenas se o produto estiver ativo e salva o nome/preço no momento do pedido """
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT nome, preco, ativo FROM produtos WHERE id = %s", (produto_id,))
            produto = cursor.fetchone()
            if produto:
                nome_produto, preco, ativo = produto
                if not ativo:
                    print("❌ Este produto está inativo e não pode ser vendido!")
                    return
                valor_total = preco * quantidade
                cursor.execute(""" 
                    INSERT INTO pedidos (produto_id, quantidade, valor_total, nome_produto, preco_unitario)
                    VALUES (%s, %s, %s, %s, %s)
                """, (produto_id, quantidade, valor_total, nome_produto, preco))
                conn.commit()
                print("✅ Pedido registrado com sucesso!")
            else:
                print("❌ Produto não encontrado!")
        except Exception as e:
            print(f"Erro ao registrar pedido: {e}")
        finally:
            cursor.close()
            conn.close()


def cancelar_pedido(pedido_id):
    """ Cancela um pedido pelo ID, mantendo-o visível na listagem """
    conn = conectar()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE pedidos SET cancelado = TRUE WHERE id = %s", (pedido_id,))
            conn.commit()
            print("✅ Pedido cancelado com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao cancelar pedido: {e}")
        finally:
            cursor.close()
            conn.close()


def listar_pedidos():
    """Lista pedidos filtrando por intervalo de datas."""
    try:
        data_inicial = input("Digite a data inicial (YYYY-MM-DD): ")
        data_final = input("Digite a data final (YYYY-MM-DD): ")

        try:
            dt_inicial = datetime.strptime(data_inicial, "%Y-%m-%d")
            dt_final = datetime.strptime(data_final, "%Y-%m-%d")
        except ValueError:
            print("❌ Formato de data inválido! Use o formato YYYY-MM-DD.")
            return

        if dt_inicial > dt_final:
            print("❌ Erro: A data inicial não pode ser maior que a data final!")
            return
        
        conn = conectar()
        if conn:
            cur = conn.cursor()

            # Alterando a consulta para usar a função DATE() para ignorar a hora
            cur.execute("""
                SELECT id, nome_produto, quantidade, valor_total, data, cancelado
                FROM pedidos
                WHERE DATE(data) BETWEEN %s AND %s
                ORDER BY data ASC
            """, (dt_inicial.date(), dt_final.date()))

            pedidos = cur.fetchall()

            if not pedidos:
                print("⚠️ Nenhum pedido encontrado no período selecionado.")
            else:
                print("\n📋 Pedidos:")
                for pedido in pedidos:
                    pedido_id, nome_produto, quantidade, valor_total, data, cancelado = pedido
                    status = "Cancelado" if cancelado else "Ativo"
                    print(f"🆔 ID: {pedido_id} | 📦 Produto: {nome_produto} | 🔢 Quantidade: {quantidade} | 💰 Valor: R${valor_total:.2f} | 📅 Data: {data.strftime('%Y-%m-%d')} | 🚩 Status: {status}")

            # Fechando a conexão
            cur.close()
            conn.close()

    except Exception as e:
        print(f"❌ Erro ao listar pedidos: {e}")
