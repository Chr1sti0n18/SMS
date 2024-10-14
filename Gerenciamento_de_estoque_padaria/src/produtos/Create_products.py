from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from PIL import Image
from dbProducts import Database 
#from Read_products import Read
#from Delete_products import DeletarProduto

class Create:

    def __init__(self):

        self.main_window = Tk()
        self.main_window.title("Cadastro de Produto")
        self.main_window.resizable(False, FALSE)
        self.main_window.geometry("600x350+620+275")
        self.main_window.iconbitmap('Gerenciamento_de_estoque_padaria/src/assets/logo_sem_fundo.ico')
        self.main_window.config(background='#EBEBEB') 
        
        # Criando frame principal
        self.frame1 = ctk.CTkFrame(self.main_window, fg_color='#EBEBEB')
        self.frame1.pack(side="top", fill="y", expand = False, ipadx = 500)
        self.inner_frame1 = ctk.CTkFrame(self.frame1, fg_color="#FFC07E")
        self.inner_frame1.pack(fill="both") 

         # Texto da frame principal
        self.head = ctk.CTkLabel(self.inner_frame1, text="Cadastro de produtos", font=ctk.CTkFont(family="Segoe Script", size=25, weight="bold"), 
                                 fg_color="#FFC07E", text_color="#554131",height=75, anchor="center")
        
        self.option_menu = ctk.CTkOptionMenu(self.frame1, values=["Categoria", "Doces", "Enlatados", "Salgados"], fg_color="#EBEBEB", 
                                                dropdown_fg_color="#EBEBEB", button_color="#EBEBEB", text_color="#554131", 
                                                    button_hover_color="#EBEBEB", font=ctk.CTkFont(family="Segoe UI", weight="bold"))
        self.option_menu.pack(side="right", expand=False)
    
        
        self.head.pack(fill="both") 

        #Criando o formulário de criação de produto
        self.frame_form = ctk.CTkFrame(self.main_window)
        self.frame_form.pack(fill="both", expand=True)
        self.inner_frame_form = ctk.CTkFrame(self.frame_form, fg_color='transparent')
        self.inner_frame_form.pack(expand=True)
        self.form_codigo = ctk.CTkEntry(self.inner_frame_form, placeholder_text="Id do produto", height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_codigo.grid(row=0, column=1 , pady=10, padx=15, sticky=E)
        self.form_name = ctk.CTkEntry(self.inner_frame_form, placeholder_text="Nome", height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_name.grid(row=0, column=2, pady=10, padx=15, sticky=W)
        self.form_price = ctk.CTkEntry(self.inner_frame_form, placeholder_text="Preço", height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_price.grid(row=1, column=1, pady=10, padx=15, sticky=E)
        self.form_qtd = ctk.CTkEntry(self.inner_frame_form, placeholder_text="Quantidade", height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_qtd.grid(row=1, column=2, pady=10, padx=15, sticky=W)
        self.form_val = ctk.CTkEntry(self.inner_frame_form, placeholder_text="Validade", height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_val.grid(row=2, column=1, pady=10, padx=15, sticky=E)
        self.form_lote = ctk.CTkEntry(self.inner_frame_form, placeholder_text="Lote", height=40, width=140, corner_radius=15, border_color="#554131")
        self.form_lote.grid(row=2, column=2, padx=14, sticky=W)
        
        self.frame_form.configure(fg_color='#EBEBEB')

        self.locate_button = ctk.CTkButton(self.inner_frame_form, text="Buscar", height=40, width=5, corner_radius=15)
        self.locate_button.grid(row=2, column=2, sticky=E)
        
        self.submit_button = ctk.CTkButton(self.inner_frame_form, text="Cadastrar", height=40, width=200, corner_radius=15)
        self.submit_button.grid(row=3, column=1, rowspan=2, columnspan=3, pady=20, padx=45)
        
        self.main_window.mainloop()
        
    def createProduct(self): 
        
        ID=self.form_codigo.get().upper()
        Produto=self.form_name.get().upper()
        Quantidade=self.form_qtd.get().upper()
        Preco=self.form_price.get().upper()
        Validade=self.form_val.get().upper()
        Categoria=self.form
        
        
    def insert(self, ID, Produto, Quantidade, Preco, Validade, Categoria, Lote):
        self.cur.execute("INSERT INTO ProdutosPadaria (ID, Produto, Quantidade, Preco, Validade, Categoria, Lote) VALUES (?, ?, ?, ?, ?, ?, ?)",
                         (ID, Produto, Quantidade, Preco, Validade, Categoria, Lote))
        self.con.commit()

create = Create()
