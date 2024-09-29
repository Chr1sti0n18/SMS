import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

class DeletarProduto:
    def __init__(self):
        self.main_window = ctk.CTk()
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        self.main_window.title("Deletar")
        self.main_window.geometry(f"{screen_width}x{screen_height}+0+0")
        self.main_window.configure(fg_color="white")
        self.main_window.resizable(False, False)

        # Carregando a logo
        logo = ctk.CTkImage(light_image=Image.open("Gerenciamento_de_estoque_padaria/src/assets/logo.png"), 
                            dark_image=Image.open("Gerenciamento_de_estoque_padaria/src/assets/logo.png"), size=(90, 90))    
        
        # Criando frame principal
        self.frame1 = ctk.CTkFrame(self.main_window)
        self.frame1.pack(side="top", fill="y", expand = False, ipadx = 1280)
        
        # Criando inner frame 
        self.inner_frame1 = ctk.CTkFrame(self.frame1)
        self.inner_frame1.pack(fill="both") 
        
        # Texto do inner frame
        self.head = ctk.CTkLabel(self.inner_frame1, text="Deletar Produto", font=("MONTSERRAT", 22, "bold"), 
                                 fg_color="#FFC07E", text_color="#554131", height=90, width=screen_width, anchor="center")
        
        #posicionando logo 
        self.image_label = ctk.CTkLabel(self.inner_frame1, image=logo, text="")
        self.image_label.pack(side="left", anchor="w")  
        
        self.head.pack(fill="both") 

        # Criando a tabela de produtos
        self.tree = ttk.Treeview(self.main_window, columns=("ID", "Nome", "Preço"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome do Produto")
        self.tree.heading("Preço", text="Preço")
        self.tree.pack(fill="both", expand=True, padx=20, pady=20)

        #adicionando dados fictícios para testes
        self.produtos = [("123456", "Pão Francês", "R$0,50"), ("7891011", "Bolo de Chocolate", "R$6,00"), ("121314", "Torta de Frango", "R$7,00")]
        for produto in self.produtos:
            self.tree.insert("", "end", values=produto)

        #botão para deletar o produto selecionado
        self.botao_deletar = ctk.CTkButton(self.main_window, text="Deletar Produto Selecionado", 
                                           command=self.deletar_produto, fg_color="#4CAF50", 
                                           text_color="black", border_width=2, border_color="black", corner_radius=8)
        self.botao_deletar.pack(pady=100)

        self.main_window.mainloop()

    def deletar_produto(self):
        # Obtém o item selecionado
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showwarning("Aviso", "Nenhum produto selecionado!")
            return

        # Pega os valores do item selecionado
        produto_selecionado = self.tree.item(selected_item, "values")

        # Confirmação
        confirmacao = messagebox.askquestion("Confirmação", f"Tem certeza que deseja deletar o produto {produto_selecionado[1]}?")
        
        if confirmacao == 'yes':
            # Deleta o produto da tabela
            self.tree.delete(selected_item)
            messagebox.showinfo("Sucesso", f"Produto '{produto_selecionado[1]}' deletado com sucesso.")
        else:
            messagebox.showinfo("Cancelado", "Exclusão do produto cancelada.")

app = DeletarProduto()