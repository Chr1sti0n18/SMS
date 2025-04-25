from tkinter import messagebox, ttk
import customtkinter as ctk
from customtkinter import *
from tkinter import *
from PIL import Image
from src import Create
from .dbProducts import Database 
import os

class Read:
    def __init__(self):
        self.db = Database("products.db")
        # Criando a estrutura da janela
        self.main_window = Tk()
        self.main_window.title("Produtos")
        self.altura = self.main_window.winfo_screenheight()
        self.largura = self.main_window.winfo_screenwidth() 
        self.main_window.state('zoomed')
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        ICON_PATH = os.path.join(BASE_DIR, '..', 'assets', 'logo_sem_fundo.ico')
        self.main_window.iconbitmap(ICON_PATH)
        self.main_window.config(background="#EBEBEB")
        self.main_window.resizable(FALSE, FALSE)

        self.largura_logo =self.largura * 0.12
        self.altura_logo =self.altura * 0.15
        # Carregando a logo
        LOGO_PATH = os.path.join(BASE_DIR, '..', 'assets', 'logotipo.png')
        logo = ctk.CTkImage(light_image=Image.open(LOGO_PATH), 
                            dark_image=Image.open(LOGO_PATH), size=(self.largura_logo, self.altura_logo))    
        
        # Criando head da aba
        self.inner_frame1 = ctk.CTkFrame(master= self.main_window, fg_color="#FFC07E", width=self.largura)
        self.inner_frame1.pack(side="top", fill="x") 

        self.altura_label = self.altura * 0.1
         # Texto do head da aba
        self.head = ctk.CTkLabel(self.inner_frame1, text="Produtos", font=CTkFont(family="Segoe Script", size=50, weight="bold"), 
                                 fg_color="#FFC07E", text_color="#554131",height=self.altura_label)
        
        # Posicionando logo no head da aba
        self.image_label = ctk.CTkLabel(text="", master=self.inner_frame1, image=logo)
        self.image_label.pack(side="left")  # Sem padding, a imagem fica na extrema esquerda
        self.head.place(relx=0.5, rely=0.5, anchor="center")
        
        # Criando barra de busca
        self.inner_frame2 = ctk.CTkFrame(self.main_window, width=self.largura)
        self.inner_frame2.configure(height=self.altura - (self.altura * 0.9), fg_color='transparent')
        self.inner_frame2.pack(fill='both', ipady=10)
        self.search_box=ctk.CTkEntry(self.inner_frame2, placeholder_text="Pesquisar", corner_radius=15, width=150, border_color="#554131", font=CTkFont(family="Segoe UI"))
        self.search_box.place(relx=0.135, rely=0.6)
        self.search_button=ctk.CTkButton(self.inner_frame2, width = self.largura - (self.largura *  0.98), text = 'Buscar', fg_color='#554131',
                                            font=ctk.CTkFont(family="Segoe UI", weight="bold"), text_color='#EBEBEB', command=self.searchProduct)
        self.search_button.place(relx=0.27, rely=0.6)
        
        #Botão de refresh
        REFRESH_PATH = os.path.join(BASE_DIR, '..', 'assets', 'refresh.png')
        self.refresh_icon=ctk.CTkImage(light_image = Image.open(REFRESH_PATH), 
                                        dark_image = Image.open(REFRESH_PATH), size=(25, 25))
        self.refresh_button=ctk.CTkButton(self.inner_frame2, width = self.largura - (self.largura * 0.98), height= 35, text = '',image=self.refresh_icon, fg_color='transparent',
                                            font=ctk.CTkFont(family="Segoe UI", weight="bold"), text_color='#EBEBEB', hover_color= "#FFF", 
                                            command=self.displayAll)
        self.refresh_button.place(relx=0.832, rely=0.6)
        
        # Seletor de categoria
        self.combobox = ctk.CTkComboBox(self.inner_frame2, values=["Todos", "Salgados", "Enlatados", "Doces"], 
                                        corner_radius=15, width=150, font=CTkFont(family="Segoe UI"), command=self.teste)
        self.combobox.place(relx=0.69, rely=0.6)
        
        
        # Criando a tabela
        self.scrollbarFrame=ctk.CTkScrollableFrame(self.main_window, orientation="vertical", fg_color='#EBEBEB')
        self.scrollbarFrame.pack(fill="x")
        self.table_frame=ctk.CTkFrame(self.scrollbarFrame, bg_color="white")
        self.table_frame.pack(anchor="center", pady=20)
        self.table_style=ttk.Style()
        self.table_style.configure("Treeview", background="#FFF", rowheight=20, fieldbackground='#EBEBEB', 
                                   font=ctk.CTkFont(family="Segoe UI", size=10))
        self.table_style.configure("Heading", font=ctk.CTkFont(family="Segoe UI", size=10))
        self.table_style.map('Treeview', background=[('selected', 'grey')])
        self.table=ttk.Treeview(self.table_frame, columns=(1, 2, 3, 4, 5, 6, 7))
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
        self.table.heading("7", text="Lote")
        self.table.column("7", minwidth=90, stretch="no", anchor="center")
        self.table["show"] = "headings"
        self.table.bind("<ButtonRelease-1>", self.pegar_dados)
        self.table.pack(fill="both")
    
        self.displayAll()
    
        # Botões da aba
        self.frame2 = ctk.CTkFrame(self.main_window, width=self.largura)
        self.frame2.configure(fg_color='transparent')
        self.frame2.pack(fill="both")
        
        self.update_button = ctk.CTkButton(self.frame2, width=150, text="Alterar", command = self.update_produto ,fg_color='#554131',
                                            font=ctk.CTkFont(family="Segoe UI", weight="bold"), text_color='#EBEBEB')
        self.update_button.place(rely=0.5, relx=0.2, anchor="center")
        
        self.botao_deletar = ctk.CTkButton(self.frame2, text="Deletar", 
                                           command=self.deletar_produto, fg_color="#554131", 
                                           text_color="#EBEBEB", width=150, font=ctk.CTkFont(family="Segoe UI", weight="bold"))
        self.botao_deletar.place(rely=0.5, relx=0.8, anchor="center")
        
        self.botao_cadastrar = ctk.CTkButton(self.frame2, text="Cadastrar", 
                                           command=self.cadastar_produto, fg_color="#554131", 
                                           text_color="#EBEBEB", width=150, font=ctk.CTkFont(family="Segoe UI", weight="bold"))
        self.botao_cadastrar.place(relx=0.5, rely=0.5, anchor="center")
    
        self.main_window.mainloop()
            
    # Dados da tabela
    def pegar_dados(self, event):
        global selected_item 
        selected_item = self.table.focus()
        data = self.table.item(selected_item)
        global row
        row = data["values"]

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
        selected_item = self.table.focus()

        if not selected_item:
            return messagebox.showwarning("Aviso", "Nenhum produto selecionado!")

        # Confirmação
        confirmacao = messagebox.askquestion("Confirmação", f"Tem certeza que deseja deletar o produto {row[1]}?")
        
        if confirmacao == 'yes':
            # Deleta o produto da tabela
            self.db.remove(row[0])
            self.displayAll()
            messagebox.showinfo("Sucesso", f"Produto '{row[1]}' deletado com sucesso.")
        else:
            messagebox.showinfo("Cancelado", "Exclusão do produto cancelada.")
            
    def cadastar_produto(self):
        Create()
                   
    def update_produto(self):
        from src import Update
        selected_item = self.table.selection()[0]   
        values = self.table.item(selected_item, "values")
        Update(values[0], values[1], values[5], values[3], values[2], values[4], values[6])          
        
        
