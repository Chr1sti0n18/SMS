from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import os

class Update:

    def __init__(self, ID, name, category, price, qtd, val, lote):

        self.ID=ID
        self.name=name
        self.price=price
        self.qtd=qtd
        self.val=val
        self.lote=lote
        
        from src import Database

        self.db = Database("products.db")
        self.main_window = Tk()
        self.main_window.title("Alteração de Produto")
        self.main_window.resizable(False, FALSE)
       
        #Tamanho da janela
        self.screen_width = self.main_window.winfo_screenwidth()
        self.screen_height = self.main_window.winfo_screenheight()
        self.width=900
        self.height=700
        self.x = (self.screen_width // 2) - (self.width // 2)
        self.y = (self.screen_height // 2) - (self.height // 2)
        self.main_window.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        ICON_PATH = os.path.join(BASE_DIR, '..', 'assets', 'logo_sem_fundo.ico')
        self.main_window.iconbitmap(ICON_PATH)
        self.main_window.config(background='#EBEBEB') 
        
        # Criando frame principal
        self.frame1 = ctk.CTkFrame(self.main_window, fg_color='#EBEBEB')
        self.frame1.pack(side="top", fill="y", expand = False, ipadx = 500)
        self.inner_frame1 = ctk.CTkFrame(self.frame1, fg_color="#FFC07E")
        self.inner_frame1.pack(fill="both") 

         # Texto da frame principal
        self.head = ctk.CTkLabel(self.inner_frame1, text="Alteração de produtos", font=ctk.CTkFont(family="Segoe Script", size=35, weight="bold"), 
                                 fg_color="#FFC07E", text_color="#554131",height=75, anchor="center")
        
    
        
        self.head.pack(fill="both") 

        #Criando o formulário de criação de produto
        self.name_label=ctk.CTkLabel(self.main_window, text="PRODUTO", font=ctk.CTkFont("Segoe UI", 15, "bold"))
        self.name_label.pack(anchor=S, pady=5)
        self.form_name = ctk.CTkEntry(self.main_window, placeholder_text="Nome", height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_name.insert(END, name)
        self.form_name.pack(anchor=N)
       
        self.frame_form = ctk.CTkFrame(self.main_window)
        self.frame_form.pack(fill="both")
        self.inner_frame_form = ctk.CTkFrame(self.frame_form, fg_color='transparent')
        
        self.inner_frame_form.pack(pady=10)
        self.form_codigo = ctk.CTkEntry(self.inner_frame_form, height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_codigo.grid(row=1, column=1, padx=15, sticky=N)
        self.ID_label=ctk.CTkLabel(self.inner_frame_form, text="ID", font=ctk.CTkFont("Segoe UI", 15, "bold"))
        self.ID_label.grid(row=0, column=1, sticky=S)
        self.form_codigo.insert(END, ID)
        self.form_codigo.configure(state="disabled")
        
        self.category_label=ctk.CTkLabel(self.inner_frame_form, text="Categoria", font=ctk.CTkFont("Segoe UI", 15, "bold"))
        self.category_label.grid(row=0, column=2)
        self.form_category = ctk.CTkEntry(self.inner_frame_form, placeholder_text="Categoria", height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_category.grid(row=1, column=2, padx=15, sticky=N)
        self.form_category.insert(END, category)
        
        self.price_label=ctk.CTkLabel(self.inner_frame_form, text="Preço", font=ctk.CTkFont("Segoe UI", 15, "bold"))
        self.price_label.grid(row=3, column=1)
        self.form_price = ctk.CTkEntry(self.inner_frame_form, placeholder_text="Preço", height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_price.grid(row=4, column=1, padx=15, sticky=E)
        self.form_price.insert(END, price)
        
        self.qtd_label=ctk.CTkLabel(self.inner_frame_form, text="Quantidade", font=ctk.CTkFont("Segoe UI", 15, "bold"))
        self.qtd_label.grid(row=3, column=2)
        self.form_qtd = ctk.CTkEntry(self.inner_frame_form, placeholder_text="Quantidade", height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_qtd.grid(row=4, column=2, padx=15, sticky=W)
        self.form_qtd.insert(END, qtd)
        
        self.val_label=ctk.CTkLabel(self.inner_frame_form, text="Validade", font=ctk.CTkFont("Segoe UI", 15, "bold"))
        self.val_label.grid(row=5, column=1)
        self.form_val = ctk.CTkEntry(self.inner_frame_form, placeholder_text="Validade", height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_val.grid(row=6, column=1, padx=15, sticky=E)
        self.form_val.insert(END, val)
        
        self.lote_label=ctk.CTkLabel(self.inner_frame_form, text="Lote", font=ctk.CTkFont("Segoe UI", 15, "bold"))
        self.lote_label.grid(row=5, column=2)
        self.form_lote = ctk.CTkEntry(self.inner_frame_form, placeholder_text="Lote", height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_lote.grid(row=6, column=2, padx=14, sticky=W)
        self.form_lote.insert(END, lote)
        
        self.frame_form.configure(fg_color='#EBEBEB')

        #Botão alterar
        self.submit_button = ctk.CTkButton(self.inner_frame_form, text="Alterar", height=40, width=200, corner_radius=15, command=self.Update_Product,
                                           fg_color="#554131", text_color="#EBEBEB", font=ctk.CTkFont(family="Segoe UI", weight="bold"))
        self.submit_button.grid(row=7, column=1, rowspan=2, columnspan=3, pady=30, padx=45)
        
        self.main_window.mainloop()
        
    def Update_Product(self):
        
        ID = self.form_codigo.get()
        Produto=self.form_name.get().upper()
        Quantidade=self.form_qtd.get()
        Preco=self.form_price.get()
        Validade=self.form_val.get()
        Categoria=self.form_category.get().upper()
        Lote=self.form_lote.get().upper()
        
        if  Produto == None or Quantidade == None or Preco == None or Validade == None or Categoria == None or Lote == None:
            self.main_window.destroy()
            messagebox.showinfo("Erro", "Não deixe nenhum campo vazio")
            Update()
        else:
            try:
                self.db.update(Produto, Quantidade, Preco, Validade, Categoria, Lote, ID)
                self.main_window.destroy()
                messagebox.showinfo("Sucesso!", "Produto alterado com sucesso!")
                
            except Exception as e:
                self.main_window.destroy()
                messagebox.showinfo("Erro", "Erro ao alterar produto: %s"%(e))    
                 