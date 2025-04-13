from tkinter import *
from tkinter import ttk, messagebox
import customtkinter as ctk
from PIL import Image
from dbProducts import Database 
from dbVendas import DatabaseVendas
#from Read_products import Read
#from Delete_products import DeletarProduto

class GetProduto:

    def __init__(self):

        self.db = Database ("products.db")
        self.dbVendas = Database ("vendas.db")
        self.main_window = Tk()
        self.main_window.title("Cadastro de Vendas")
        self.main_window.resizable(False, FALSE)
       
        #Tamanho da janela
        self.screen_width = self.main_window.winfo_screenwidth()
        self.screen_height = self.main_window.winfo_screenheight()
        self.width=450
        self.height=350
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
        self.head = ctk.CTkLabel(self.inner_frame1, text="$ Iniciar Venda $", font=ctk.CTkFont(family="Segoe Script", size=35, weight="bold"), 
                                 fg_color="#FFC07E", text_color="#554131",height=75, anchor="center")
        
        self.head.pack(fill="both") 

        #Expansão de tela, elementos na primeira tela estão abaixo da função
        def segundaTela():
            #Dados do produto
            produto = self.db.searchID(self.form_id.get())

            self.head.configure(text = "Confirmação")
            
            #Alteração tamanho da janela
            self.width=700
            self.height=500
            self.x = (self.screen_width // 2) - (self.width // 2)
            self.y = (self.screen_height // 2) - (self.height // 2)
            self.main_window.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
            
            self.frame_form = ctk.CTkFrame(self.main_window, fg_color='#EBEBEB')
            self.frame_form.pack(fill="both")
            self.inner_frame_form = ctk.CTkFrame(self.frame_form, fg_color='transparent')
            self.inner_frame_form.pack(pady = 25)
            
            #Criando campos com informações, preenchimento desabilitado
            self.name_label=ctk.CTkLabel(self.inner_frame_form, text="Nome", font=ctk.CTkFont("Segoe UI", 15, "bold"))
            self.name_label.grid(row=0, column=1, columnspan = 2)
            self.form_name = ctk.CTkEntry(self.inner_frame_form, height=40, width=435, corner_radius=15, border_color="#554131", justify = "center")
            self.form_name.grid(row=1, column=1, padx=15, sticky=N, columnspan = 2)
            self.form_name.insert(END, produto[1])
            nome = self.form_name.get()
            self.form_name.configure(state = "disabled")
            
            self.price_label=ctk.CTkLabel(self.inner_frame_form, text="Valor Unidade", font=ctk.CTkFont("Segoe UI", 15, "bold"))
            self.price_label.grid(row=3, column=1, columnspan = 2)
            self.form_price = ctk.CTkEntry(self.inner_frame_form, height=40, width=435, corner_radius=15, border_color="#554131", justify = "center")
            self.form_price.grid(row=4, column=1, padx=15, sticky=E, columnspan = 2)
            self.form_price.insert(END, produto[3])
            preco = float(self.form_price.get())
            self.form_price.configure(state = "disabled")
            
            self.valtotal_label=ctk.CTkLabel(self.inner_frame_form, text="Valor Total", font=ctk.CTkFont("Segoe UI", 15, "bold"))
            self.valtotal_label.grid(row=5, column=1, columnspan = 2)
            self.form_valtotal = ctk.CTkEntry(self.inner_frame_form, height=40, width=435, corner_radius=15, border_color="#554131", justify = "center")
            self.form_valtotal.grid(row=6, column=1, padx=14, sticky=W, columnspan = 2)
            quantidade = self.form_qtd.get()
            total = float(quantidade) * float(produto[3])
            self.form_valtotal.insert(END, total)
            self.form_valtotal.configure(state = "disabled")
            
            self.form_id.configure(state = "disabled", justify = "center")
            
            #Mudando posição do botão
            self.submit_button.pack_forget()
            self.submit_button.configure(text = "Confirmar", width = 435)
            self.submit_button.pack(pady = 25)
            self.qtd_label.pack_forget()
            self.form_qtd.pack_forget()
            
            self.main_window.update()
            
        #Criando o formulário de criação de produto
        self.id_label=ctk.CTkLabel(self.main_window, text="Produto", font=ctk.CTkFont("Segoe UI", 15, "bold"))
        self.id_label.pack(anchor=S, pady = 8)
        self.form_id = ctk.CTkEntry(self.main_window, height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_id.pack(anchor=N)
        id = self.form_id.get()
        
        self.qtd_label=ctk.CTkLabel(self.main_window, text="Quantidade", font=ctk.CTkFont("Segoe UI", 15, "bold"))
        self.qtd_label.pack(anchor = S, pady = 8)
        self.form_qtd = ctk.CTkEntry(self.main_window, height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_qtd.pack(anchor = N)
        qtd = self.form_qtd.get()
        
        #Botão cadastrar
        self.submit_button = ctk.CTkButton(self.main_window, text="Cadastrar", height=40, width=100, corner_radius=15, command=segundaTela, 
                                           fg_color="#554131", text_color="#EBEBEB", font=ctk.CTkFont(family="Segoe UI", weight="bold"))
        self.submit_button.pack(pady = 25)
        self.main_window.mainloop()
        
        # def cadastrarVenda(self):
        #     self.dbVendas.insert()
                 
    #     #Botão cadastrar
    #     self.submit_button = ctk.CTkButton(self.inner_frame_form, text="Cadastrar", height=40, width=200, corner_radius=15, command=self.createProduct, 
    #                                        fg_color="#554131", text_color="#EBEBEB", font=ctk.CTkFont(family="Segoe UI", weight="bold"))
    #     self.submit_button.grid(row=7, column=1, rowspan=2, columnspan=3, pady=30, padx=45)
        
    #     #Função Criar Produto
    # def createProduct(self): 
    #     ID=self.form_codigo.get()
    #     Produto=self.form_name.get().upper()
    #     Quantidade=self.form_qtd.get()
    #     Preco=self.form_price.get()
    #     Validade=self.form_val.get()
    #     Categoria=self.form_category.get().upper()
    #     Lote=self.form_lote.get().upper()
    
    #     if ID == None or Produto == None or Quantidade == None or Preco == None or Validade == None or Categoria == "CATEGORIA" or Lote == None:
    #         self.main_window.destroy()
    #         messagebox.showinfo("Erro", "Não deixe nenhum campo vazio")
    #         GetProduto()
    #     else:
    #         try:
    #             self.db.insert(ID, Produto, Quantidade, Preco, Validade, Categoria, Lote)
    #             self.main_window.destroy()
    #             messagebox.showinfo("Sucesso!", "Produto cadastrado com sucesso!")
    #             GetProduto()
    #         except Exception as e:
    #             self.main_window.destroy()
    #             messagebox.showinfo("Erro", "Erro ao cadastrar produto: %s"%(e))
    #             GetProduto()
    
GetProduto()