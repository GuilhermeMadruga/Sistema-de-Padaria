import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import tkinter.ttk as ttk
from database import (
    cadastrar_produto, inativar_produto, editar_produto,
    registrar_pedido, listar_pedidos, cancelar_pedido
)

def centralizar_tela(tela, largura, altura):
    """ Função para centralizar a tela """
    screen_width = tela.winfo_screenwidth()
    screen_height = tela.winfo_screenheight()
    position_top = int(screen_height / 2 - altura / 2)
    position_right = int(screen_width / 2 - largura / 2)
    tela.geometry(f'{largura}x{altura}+{position_right}+{position_top}')

def fechar_todas_janelas(root):
    """ Fecha todas as janelas abertas """
    for window in root.winfo_children():
        window.destroy()

def menu_principal():
    """ Tela principal com opções """
    root = tk.Tk()
    root.title("🍞 Padaria System")
    centralizar_tela(root, 300, 300)

    def abrir_menu_gerenciar_produtos():
        """ Abre o menu de gerenciamento de produtos """
        fechar_todas_janelas(root)
        
        gerenciar_produtos_window = tk.Toplevel(root)
        gerenciar_produtos_window.title("📦 Gerenciamento de Produtos")
        centralizar_tela(gerenciar_produtos_window, 300, 300)

        def abrir_tela_cadastrar_produto():
            """ Abre tela específica para cadastro de produto """
            gerenciar_produtos_window.destroy()
            
            cadastrar_produto_window = tk.Toplevel(root)
            cadastrar_produto_window.title("📦 Cadastrar Produto")
            centralizar_tela(cadastrar_produto_window, 300, 250)

            tk.Label(cadastrar_produto_window, text="Nome do produto:").pack()
            nome_entry = tk.Entry(cadastrar_produto_window)
            nome_entry.pack()

            tk.Label(cadastrar_produto_window, text="Preço do produto:").pack()
            preco_entry = tk.Entry(cadastrar_produto_window)
            preco_entry.pack()

            def salvar_cadastro():
                """ Salva o cadastro do produto """
                nome = nome_entry.get()
                try:
                    preco = float(preco_entry.get())
                    cadastrar_produto(nome, preco)
                    messagebox.showinfo("Cadastro", "✅ Produto cadastrado com sucesso!")
                    cadastrar_produto_window.destroy()
                    abrir_menu_gerenciar_produtos()
                except ValueError:
                    messagebox.showerror("Erro", "Preço inválido. Use números.")

            def cancelar_cadastro():
                """ Cancela o cadastro e volta ao menu anterior """
                cadastrar_produto_window.destroy()
                abrir_menu_gerenciar_produtos()

            tk.Button(cadastrar_produto_window, text="Salvar", command=salvar_cadastro).pack(pady=10)
            tk.Button(cadastrar_produto_window, text="Cancelar", command=cancelar_cadastro).pack(pady=5)

        def abrir_tela_editar_produto():
            """ Abre tela específica para edição de produto """
            gerenciar_produtos_window.destroy()
            
            editar_produto_window = tk.Toplevel(root)
            editar_produto_window.title("📦 Editar Produto")
            centralizar_tela(editar_produto_window, 300, 300)

            tk.Label(editar_produto_window, text="ID do produto:").pack()
            produto_id_entry = tk.Entry(editar_produto_window)
            produto_id_entry.pack()

            tk.Label(editar_produto_window, text="Novo nome:").pack()
            novo_nome_entry = tk.Entry(editar_produto_window)
            novo_nome_entry.pack()

            tk.Label(editar_produto_window, text="Novo preço:").pack()
            novo_preco_entry = tk.Entry(editar_produto_window)
            novo_preco_entry.pack()

            def salvar_edicao():
                """ Salva a edição do produto """
                try:
                    produto_id = int(produto_id_entry.get())
                    novo_nome = novo_nome_entry.get()
                    novo_preco = float(novo_preco_entry.get())
                    editar_produto(produto_id, novo_nome, novo_preco)
                    messagebox.showinfo("Editar", "✅ Produto editado com sucesso!")
                    editar_produto_window.destroy()
                    abrir_menu_gerenciar_produtos()
                except ValueError:
                    messagebox.showerror("Erro", "ID ou preço inválido.")

            def cancelar_edicao():
                """ Cancela a edição e volta ao menu anterior """
                editar_produto_window.destroy()
                abrir_menu_gerenciar_produtos()

            tk.Button(editar_produto_window, text="Salvar", command=salvar_edicao).pack(pady=10)
            tk.Button(editar_produto_window, text="Cancelar", command=cancelar_edicao).pack(pady=5)

        def abrir_tela_inativar_produto():
            """ Abre tela específica para inativar produto """
            gerenciar_produtos_window.destroy()
            
            inativar_produto_window = tk.Toplevel(root)
            inativar_produto_window.title("📦 Inativar Produto")
            centralizar_tela(inativar_produto_window, 300, 200)

            tk.Label(inativar_produto_window, text="ID do produto:").pack()
            produto_id_entry = tk.Entry(inativar_produto_window)
            produto_id_entry.pack()

            def confirmar_inativacao():
                """ Confirma a inativação do produto """
                try:
                    produto_id = int(produto_id_entry.get())
                    inativar_produto(produto_id)
                    messagebox.showinfo("Inativar", "✅ Produto inativado com sucesso!")
                    inativar_produto_window.destroy()
                    abrir_menu_gerenciar_produtos()
                except ValueError:
                    messagebox.showerror("Erro", "ID inválido.")

            def cancelar_inativacao():
                """ Cancela a inativação e volta ao menu anterior """
                inativar_produto_window.destroy()
                abrir_menu_gerenciar_produtos()

            tk.Button(inativar_produto_window, text="Inativar", command=confirmar_inativacao).pack(pady=10)
            tk.Button(inativar_produto_window, text="Cancelar", command=cancelar_inativacao).pack(pady=5)

        def voltar_menu_principal():
            """ Volta ao menu principal """
            gerenciar_produtos_window.destroy()
            menu_principal()

        # Botões do menu de gerenciamento de produtos
        tk.Button(gerenciar_produtos_window, text="Cadastrar Produto", command=abrir_tela_cadastrar_produto).pack(pady=10)
        tk.Button(gerenciar_produtos_window, text="Editar Produto", command=abrir_tela_editar_produto).pack(pady=10)
        tk.Button(gerenciar_produtos_window, text="Inativar Produto", command=abrir_tela_inativar_produto).pack(pady=10)
        tk.Button(gerenciar_produtos_window, text="Voltar", command=voltar_menu_principal).pack(pady=10)

    def abrir_menu_gerenciar_pedidos():
        """ Abre o menu de gerenciamento de pedidos """
        fechar_todas_janelas(root)
        
        gerenciar_pedidos_window = tk.Toplevel(root)
        gerenciar_pedidos_window.title("🛒 Gerenciamento de Pedidos")
        centralizar_tela(gerenciar_pedidos_window, 300, 300)

        def abrir_tela_registrar_pedido():
            """ Abre tela específica para registrar pedido """
            gerenciar_pedidos_window.destroy()
            
            registrar_pedido_window = tk.Toplevel(root)
            registrar_pedido_window.title("🛒 Registrar Pedido")
            centralizar_tela(registrar_pedido_window, 300, 250)

            tk.Label(registrar_pedido_window, text="ID do produto:").pack()
            produto_id_entry = tk.Entry(registrar_pedido_window)
            produto_id_entry.pack()

            tk.Label(registrar_pedido_window, text="Quantidade:").pack()
            quantidade_entry = tk.Entry(registrar_pedido_window)
            quantidade_entry.pack()

            def salvar_pedido():
                """ Salva o registro do pedido """
                try:
                    produto_id = int(produto_id_entry.get())
                    quantidade = int(quantidade_entry.get())
                    registrar_pedido(produto_id, quantidade)
                    messagebox.showinfo("Pedido", "✅ Pedido registrado com sucesso!")
                    registrar_pedido_window.destroy()
                    abrir_menu_gerenciar_pedidos()
                except ValueError:
                    messagebox.showerror("Erro", "ID ou quantidade inválidos.")

            def cancelar_registro():
                """ Cancela o registro e volta ao menu anterior """
                registrar_pedido_window.destroy()
                abrir_menu_gerenciar_pedidos()

            tk.Button(registrar_pedido_window, text="Salvar", command=salvar_pedido).pack(pady=10)
            tk.Button(registrar_pedido_window, text="Cancelar", command=cancelar_registro).pack(pady=5)

        def abrir_tela_cancelar_pedido():
            """ Abre tela específica para cancelar pedido """
            gerenciar_pedidos_window.destroy()
            
            cancelar_pedido_window = tk.Toplevel(root)
            cancelar_pedido_window.title("🛒 Cancelar Pedido")
            centralizar_tela(cancelar_pedido_window, 300, 200)

            tk.Label(cancelar_pedido_window, text="ID do pedido:").pack()
            pedido_id_entry = tk.Entry(cancelar_pedido_window)
            pedido_id_entry.pack()

            def confirmar_cancelamento():
                """ Confirma o cancelamento do pedido """
                try:
                    pedido_id = int(pedido_id_entry.get())
                    cancelar_pedido(pedido_id)
                    messagebox.showinfo("Cancelar Pedido", "✅ Pedido cancelado com sucesso!")
                    cancelar_pedido_window.destroy()
                    abrir_menu_gerenciar_pedidos()
                except ValueError:
                    messagebox.showerror("Erro", "ID do pedido inválido.")

            def voltar_menu_pedidos():
                """ Volta ao menu de pedidos sem cancelar """
                cancelar_pedido_window.destroy()
                abrir_menu_gerenciar_pedidos()

            tk.Button(cancelar_pedido_window, text="Cancelar Pedido", command=confirmar_cancelamento).pack(pady=10)
            tk.Button(cancelar_pedido_window, text="Voltar", command=voltar_menu_pedidos).pack(pady=5)

        def abrir_tela_listar_pedidos():
            """ Abre tela específica para listar pedidos """
            gerenciar_pedidos_window.destroy()
            
            listar_pedidos_window = tk.Toplevel(root)
            listar_pedidos_window.title("🛒 Listar Pedidos")
            centralizar_tela(listar_pedidos_window, 800, 500)  # Aumentei o tamanho para melhor visualização

            # Frame para organizar os elementos
            frame_filtro = tk.Frame(listar_pedidos_window)
            frame_filtro.pack(pady=10, padx=10, fill='x')

            tk.Label(frame_filtro, text="Data Inicial (YYYY-MM-DD):").grid(row=0, column=0, padx=5)
            data_inicial_entry = tk.Entry(frame_filtro, width=15)
            data_inicial_entry.grid(row=0, column=1, padx=5)

            tk.Label(frame_filtro, text="Data Final (YYYY-MM-DD):").grid(row=0, column=2, padx=5)
            data_final_entry = tk.Entry(frame_filtro, width=15)
            data_final_entry.grid(row=0, column=3, padx=5)

            # Frame para a tabela com barras de rolagem
            frame_tabela = tk.Frame(listar_pedidos_window)
            frame_tabela.pack(padx=10, pady=10, fill='both', expand=True)

            # Criando Treeview com barras de rolagem
            # Barra de rolagem vertical
            scrollbar_vertical = tk.Scrollbar(frame_tabela, orient='vertical')
            scrollbar_vertical.pack(side='right', fill='y')

            # Barra de rolagem horizontal
            scrollbar_horizontal = tk.Scrollbar(frame_tabela, orient='horizontal')
            scrollbar_horizontal.pack(side='bottom', fill='x')

            # Treeview
            pedidos_tree = tk.ttk.Treeview(
                frame_tabela, 
                columns=(
                    'ID', 'Produto', 'Quantidade', 
                    'Valor Total', 'Data', 'Status'
                ), 
                show='headings',
                yscrollcommand=scrollbar_vertical.set,
                xscrollcommand=scrollbar_horizontal.set
            )

            # Configurando colunas
            pedidos_tree.column('ID', width=50, anchor='center')
            pedidos_tree.column('Produto', width=200, anchor='w')
            pedidos_tree.column('Quantidade', width=100, anchor='center')
            pedidos_tree.column('Valor Total', width=100, anchor='e')
            pedidos_tree.column('Data', width=100, anchor='center')
            pedidos_tree.column('Status', width=100, anchor='center')

            # Cabeçalhos das colunas
            pedidos_tree.heading('ID', text='ID')
            pedidos_tree.heading('Produto', text='Produto')
            pedidos_tree.heading('Quantidade', text='Quantidade')
            pedidos_tree.heading('Valor Total', text='Valor Total')
            pedidos_tree.heading('Data', text='Data')
            pedidos_tree.heading('Status', text='Status')

            # Configurando barras de rolagem
            scrollbar_vertical.config(command=pedidos_tree.yview)
            scrollbar_horizontal.config(command=pedidos_tree.xview)

            # Empacotando a Treeview
            pedidos_tree.pack(side='left', fill='both', expand=True)

            def executar_listagem():
                # Limpa resultados anteriores
                for i in pedidos_tree.get_children():
                    pedidos_tree.delete(i)
                
                data_inicial = data_inicial_entry.get() or None
                data_final = data_final_entry.get() or None
                
                try:
                    # Lista os pedidos
                    pedidos = listar_pedidos(data_inicial, data_final)
                    
                    if pedidos:
                        for pedido in pedidos:
                            pedido_id, nome_produto, quantidade, valor_total, data, cancelado = pedido
                            status = "Cancelado" if cancelado else "Ativo"
                            
                            # Insere na tabela
                            pedidos_tree.insert('', 'end', values=(
                                pedido_id, 
                                nome_produto, 
                                quantidade, 
                                f'R$ {valor_total:.2f}', 
                                data.strftime('%Y-%m-%d'), 
                                status
                            ))
                    else:
                        pedidos_tree.insert('', 'end', values=('', 'Nenhum pedido encontrado', '', '', '', ''))

                except Exception as e:
                    pedidos_tree.insert('', 'end', values=('', f'Erro: {str(e)}', '', '', '', ''))

            # Botão de listar
            botao_listar = tk.Button(
                listar_pedidos_window, 
                text="Listar Pedidos", 
                command=executar_listagem
            )
            botao_listar.pack(pady=10)

            # Botão de voltar
            botao_voltar = tk.Button(
                listar_pedidos_window, 
                text="Voltar", 
                command=listar_pedidos_window.destroy
            )
            botao_voltar.pack(pady=5)

        def voltar_menu_principal():
            """ Volta ao menu principal """
            gerenciar_pedidos_window.destroy()
            menu_principal()

        # Botões do menu de gerenciamento de pedidos
        tk.Button(gerenciar_pedidos_window, text="Registrar Pedido", command=abrir_tela_registrar_pedido).pack(pady=10)
        tk.Button(gerenciar_pedidos_window, text="Cancelar Pedido", command=abrir_tela_cancelar_pedido).pack(pady=10)
        tk.Button(gerenciar_pedidos_window, text="Listar Pedidos", command=abrir_tela_listar_pedidos).pack(pady=10)
        tk.Button(gerenciar_pedidos_window, text="Voltar", command=voltar_menu_principal).pack(pady=10)

    # Botões do menu principal
    tk.Button(root, text="Gerenciar Produtos", command=abrir_menu_gerenciar_produtos).pack(pady=10)
    tk.Button(root, text="Gerenciar Pedidos", command=abrir_menu_gerenciar_pedidos).pack(pady=10)
    tk.Button(root, text="Sair", command=root.quit).pack(pady=10)

    centralizar_tela(root, 300, 300)
    root.mainloop()

if __name__ == "__main__":
    menu_principal()




