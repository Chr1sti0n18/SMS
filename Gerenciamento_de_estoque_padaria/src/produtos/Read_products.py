from tkinter import messagebox, ttk
import customtkinter as ctk
from customtkinter import *
from tkinter import *
from PIL import Image
from dbProducts import Database 

class Read:
    def __init__(self):
        
        self.db = Database ("products.db")
        # Criando a estrutura da janela
        self.main_window = Tk()
        self.main_window.title("Produtos")
        self.main_window.state('zoomed')
        self.main_window.iconbitmap('Gerenciamento_de_estoque_padaria/src/assets/logo_sem_fundo.ico')
        self.main_window.config(background="#EBEBEB")
        self.main_window.resizable(800, FALSE)

        # Carregando a logo
        logo = ctk.CTkImage(light_image=Image.open("Gerenciamento_de_estoque_padaria/src/assets/logotipo.png"), 
                            dark_image=Image.open("Gerenciamento_de_estoque_padaria/src/assets/logotipo.png"), size=(120, 120))    
        
        # Criando frame principal
        self.frame1 = ctk.CTkFrame(self.main_window)
        self.frame1.configure(fg_color='transparent')
        self.frame1.pack(side="top", fill="y", expand = False, ipadx = 1280)
        
        # Criando head da aba
        self.inner_frame1 = ctk.CTkFrame(self.frame1)
        self.inner_frame1.configure(fg_color='#EBEBEB')
        self.inner_frame1 = ctk.CTkFrame(self.frame1, fg_color="#FFC07E")
        self.inner_frame1.pack(fill="both") 
        self.option_menu = ctk.CTkOptionMenu(self.inner_frame1, values=["Home", "Produtos", "Criação de Produtos"], fg_color="#EBEBEB", 
                                                dropdown_fg_color="#EBEBEB", button_color="#EBEBEB", text_color="#554131", 
                                                    button_hover_color="#EBEBEB", font=ctk.CTkFont(family="Segoe UI", weight="bold"))
        self.option_menu.pack(side="right", anchor="w", padx=10, expand=False)
        
         # Texto do head da aba
        self.head = ctk.CTkLabel(self.inner_frame1, text="Produtos", font=CTkFont(family="Segoe Script", size=52, weight="bold"), 
                                 fg_color="#FFC07E", text_color="#554131",height=120, anchor="center")
        
        # Posicionando logo no head da aba
        self.image_label = ctk.CTkLabel(self.inner_frame1, image=logo, text='')
        self.image_label.pack(side="left", anchor="w")  # Sem padding, a imagem fica na extrema esquerda
        self.inner_frame1.pack(fill="both")
        self.head.pack(fill="both", anchor='center') 
        
        # Criando barra de busca
        self.inner_frame2 = ctk.CTkFrame(self.frame1)
        self.inner_frame2.configure(height=600, fg_color='transparent')
        self.search_box=ctk.CTkEntry(self.inner_frame2, placeholder_text="Pesquisar", corner_radius=15, width=150, border_color="#554131", font=CTkFont(family="Segoe UI"))
        self.search_box.pack(side='left', padx=205)
        self.inner_frame2.pack(fill='both', ipadx=305, pady=10)
        self.search_button=ctk.CTkButton(self.inner_frame2, width = 75, text = 'Buscar', fg_color='#554131',
                                            font=ctk.CTkFont(family="Segoe UI", weight="bold"), text_color='#EBEBEB', command=self.searchProduct)
        self.search_button.place(relx=1, x=-1150, y=2, anchor = NE)
        
        # Seletor de categoria
        self.combobox = ctk.CTkComboBox(self.inner_frame2, values=["Todos", "Salgados", "Enlatados", "Doces"], 
                                        corner_radius=15, width=150, font=CTkFont(family="Segoe UI"), command=self.teste)
        self.combobox.pack(side='right', padx=205)
        
        
        # Criando a tabela
        self.table_frame=ctk.CTkFrame(self.main_window, bg_color="white")
        self.table_frame.pack(anchor="center", pady=15)
        self.table_style=ttk.Style()
        self.table_style.configure("Treeview", background="#EBEBEB", rowheight=20, fieldbackground='#EBEBEB', 
                                   font=ctk.CTkFont(family="Segoe UI", size=10))
        self.table_style.configure("Heading", font=ctk.CTkFont(family="Segoe UI", size=10))
        self.table_style.map('Treeview', background=[('selected', 'grey')])
        self.table=ttk.Treeview(self.table_frame, columns=(1, 2, 3, 4, 5, 6))
        
        # Criando as colunas da tabela
        self.table.heading("1", text="ID")
        self.table.column("1", width=180, stretch="no", anchor="center")
        self.table.heading("2", text="PRODUTO")
        self.table.column("2", minwidth=120, stretch="no", anchor="center")
        self.table.heading("3", text="QUANTIDADE")
        self.table.column("3", minwidth=40, stretch="no", anchor="center")
        self.table.heading("4", text="PRECO")
        self.table.column("4", minwidth=60, stretch="no", anchor="center")
        self.table.heading("5", text="VALIDADE")
        self.table.column("5", minwidth=90, stretch="no", anchor="center")
        self.table.heading("6", text="Categoria")
        self.table.column("6", minwidth=90, stretch="no", anchor="center")
        self.table["show"] = "headings"
        self.table.pack(fill="both")
        self.displayAll()
    
        # Botões da aba
        self.frame2 = ctk.CTkFrame(self.main_window)
        self.frame2.configure(fg_color='transparent')
        self.frame2.pack(fill="both", expand = False, ipadx = 1280)
        self.inner_frame3=ctk.CTkFrame(self.frame2)
        self.inner_frame3.configure(fg_color='transparent')
        self.inner_frame3.pack(side='left', fill='both')
        self.refresh_button = ctk.CTkButton(self.inner_frame3, width=150, text="Atualizar", command = self.displayAll ,fg_color='#554131',
                                            font=ctk.CTkFont(family="Segoe UI", weight="bold"), text_color='#EBEBEB')
        self.refresh_button.pack(side='right', padx=205)
        self.botao_deletar = ctk.CTkButton(self.inner_frame3, text="Deletar", 
                                           command=self.deletar_produto, fg_color="#554131", 
                                           text_color="#EBEBEB", width=150, font=ctk.CTkFont(family="Segoe UI", weight="bold"))
        self.botao_deletar.pack(side='right', padx=55)
    
        self.main_window.mainloop()
        
    # Dados da tabela
    def teste (self, choice):
        self.table.delete(*self.table.get_children())
        for row in self.db.fetch(choice):
            self.table.insert("", END, values = row)
        
    def displayAll(self):
        filter = self.combobox.get()
        self.table.delete(*self.table.get_children())
        for row in self.db.fetch(filter):
            self.table.insert("", END, values = row)

    def searchProduct(self):
        search = self.search_box.get().upper()
        self.table.delete(*self.table.get_children())
        if search == '':
            for row in self.db.fetch('Todos'):
                self.table.insert("", END, values = row)
        for row in self.db.search(search):
            self.table.insert("", END, values = row)

    def deletar_produto(self):
        # Obtém o item selecionado
        selected_item = self.table.selection()

        if not selected_item:
            messagebox.showwarning("Aviso", "Nenhum produto selecionado!")
            return

        # Pega os valores do item selecionado
        produto_selecionado = self.table.item(selected_item, "values")

        # Confirmação
        confirmacao = messagebox.askquestion("Confirmação", f"Tem certeza que deseja deletar o produto {produto_selecionado[1]}?")
        
        if confirmacao == 'yes':
            # Deleta o produto da tabela
            self.table.delete(selected_item)
            messagebox.showinfo("Sucesso", f"Produto '{produto_selecionado[1]}' deletado com sucesso.")
        else:
            messagebox.showinfo("Cancelado", "Exclusão do produto cancelada.")
            
                  
        
app=Read()
        
