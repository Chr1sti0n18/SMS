from tkinter import *
from tkinter import ttk, messagebox
import customtkinter as ctk
from PIL import Image
from .dbProducts import Database 
#from Read_products import Read
#from Delete_products import DeletarProduto

class Create:

    def __init__(self):

        self.db = Database("products.db")
        self.main_window = Tk()
        self.main_window.title("Cadastro de Produto")
        self.main_window.resizable(False, FALSE)
       
        #Tamanho da janela
        self.screen_width = self.main_window.winfo_screenwidth()
        self.screen_height = self.main_window.winfo_screenheight()
        self.width=700
        self.height=500
        self.x = (self.screen_width // 2) - (self.width // 2)
        self.y = (self.screen_height // 2) - (self.height // 2)
        self.main_window.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        
        self.main_window.iconbitmap('Gerenciamento_de_estoque_padaria/src/assets/logo_sem_fundo.ico')
        self.main_window.config(background='#EBEBEB') 
        
        # Criando frame principal
        self.frame1 = ctk.CTkFrame(self.main_window, fg_color='#EBEBEB')
        self.frame1.pack(side="top", fill="y", expand = False, ipadx = 500)
        self.inner_frame1 = ctk.CTkFrame(self.frame1, fg_color="#FFC07E")
        self.inner_frame1.pack(fill="both") 

         # Texto da frame principal
        self.head = ctk.CTkLabel(self.inner_frame1, text="Cadastro de produtos", font=ctk.CTkFont(family="Segoe Script", size=35, weight="bold"), 
                                 fg_color="#FFC07E", text_color="#554131",height=75, anchor="center")
        
        self.head.pack(fill="both") 

        #Criando o formulário de criação de produto
        self.name_label=ctk.CTkLabel(self.main_window, text="Produto", font=ctk.CTkFont("Segoe UI", 15, "bold"))
        self.name_label.pack(anchor=S, pady = 8)
        self.form_name = ctk.CTkEntry(self.main_window, height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_name.pack(anchor=N)
       
        self.frame_form = ctk.CTkFrame(self.main_window, fg_color='#EBEBEB')
        self.frame_form.pack(fill="both")
        self.inner_frame_form = ctk.CTkFrame(self.frame_form, fg_color='transparent')
        
        self.inner_frame_form.pack()
        self.form_codigo = ctk.CTkEntry(self.inner_frame_form, height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_codigo.grid(row=1, column=1, padx=15, sticky=N)
        self.ID_label=ctk.CTkLabel(self.inner_frame_form, text="ID", font=ctk.CTkFont("Segoe UI", 15, "bold"))
        self.ID_label.grid(row=0, column=1, sticky=S)
        
        self.category_label=ctk.CTkLabel(self.inner_frame_form, text="Categoria", font=ctk.CTkFont("Segoe UI", 15, "bold"))
        self.category_label.grid(row=0, column=2)
        self.form_category = ctk.CTkEntry(self.inner_frame_form, height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_category.grid(row=1, column=2, padx=15, sticky=N)
        
        self.price_label=ctk.CTkLabel(self.inner_frame_form, text="Preço", font=ctk.CTkFont("Segoe UI", 15, "bold"))
        self.price_label.grid(row=3, column=1)
        self.form_price = ctk.CTkEntry(self.inner_frame_form, height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_price.grid(row=4, column=1, padx=15, sticky=E)
        
        self.qtd_label=ctk.CTkLabel(self.inner_frame_form, text="Quantidade", font=ctk.CTkFont("Segoe UI", 15, "bold"))
        self.qtd_label.grid(row=3, column=2)
        self.form_qtd = ctk.CTkEntry(self.inner_frame_form, height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_qtd.grid(row=4, column=2, padx=15, sticky=W)
        
        self.val_label=ctk.CTkLabel(self.inner_frame_form, text="Validade", font=ctk.CTkFont("Segoe UI", 15, "bold"))
        self.val_label.grid(row=5, column=1)
        self.form_val = ctk.CTkEntry(self.inner_frame_form, height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_val.grid(row=6, column=1, padx=15, sticky=E)

        self.lote_label=ctk.CTkLabel(self.inner_frame_form, text="Lote", font=ctk.CTkFont("Segoe UI", 15, "bold"))
        self.lote_label.grid(row=5, column=2)
        self.form_lote = ctk.CTkEntry(self.inner_frame_form, height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_lote.grid(row=6, column=2, padx=14, sticky=W)
        
        #Botão cadastrar
        self.submit_button = ctk.CTkButton(self.inner_frame_form, text="Cadastrar", height=40, width=200, corner_radius=15, command=self.createProduct, 
                                           fg_color="#554131", text_color="#EBEBEB", font=ctk.CTkFont(family="Segoe UI", weight="bold"))
        self.submit_button.grid(row=7, column=1, rowspan=2, columnspan=3, pady=30, padx=45)
        
        self.main_window.mainloop()
        
        
        #Função Criar Produto
    def createProduct(self): 
        ID=self.form_codigo.get()
        Produto=self.form_name.get().upper()
        Quantidade=self.form_qtd.get()
        Preco=self.form_price.get()
        Validade=self.form_val.get()
        Categoria=self.form_category.get().upper()
        Lote=self.form_lote.get().upper()
    
        if ID == None or Produto == None or Quantidade == None or Preco == None or Validade == None or Categoria == "CATEGORIA" or Lote == None:
            self.main_window.destroy()
            messagebox.showinfo("Erro", "Não deixe nenhum campo vazio")
            Create()
        else:
            try:
                self.db.insert(ID, Produto, Quantidade, Preco, Validade, Categoria, Lote)
                self.main_window.destroy()
                messagebox.showinfo("Sucesso!", "Produto cadastrado com sucesso!")
                Create()
            except Exception as e:
                self.main_window.destroy()
                messagebox.showinfo("Erro", "Erro ao cadastrar produto: %s"%(e))
                Create()