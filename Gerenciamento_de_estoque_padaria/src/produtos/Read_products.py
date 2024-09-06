import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image

class Read:
    def __init__(self):
        # Criando a estrutura da janela
        self.main_window = ctk.CTk()
        self.main_window.title("Produtos")
        self.main_window.geometry("1280x720+0+0")
        self.main_window.configure(fg_color="#EBEBEB")
        self.main_window.state("zoomed")  
        
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
        self.head = ctk.CTkLabel(self.inner_frame1, text="Produtos", font=("MONTSERRAT", 22, "bold"), 
                                 fg_color="#FFC07E", text_color="#554131",height=90, width=1280, anchor="center")
        
        # Posicionando logo no inner frame
        self.image_label = ctk.CTkLabel(self.inner_frame1, image=logo, text="")
        self.image_label.pack(side="left", anchor="w")  # Sem padding, a imagem fica na extrema esquerda
        
        self.head.pack(fill="both") 
        
        # Criando a tabela
        self.table_frame=ctk.CTkFrame(self.main_window, bg_color="white")
        self.table_frame.pack(anchor="center", pady=25)
        self.table_style=ttk.Style()
        self.table=ttk.Treeview(self.table_frame, columns=(1, 2, 3, 4, 5))
        
        # Criando as colunas da tabela
        self.table.heading("1", text="ID")
        self.table.column("1", width=60, stretch="no", anchor="center")
        self.table.heading("2", text="PRODUTO")
        self.table.column("2", minwidth=120, stretch="no", anchor="center")
        self.table.heading("3", text="QUANT")
        self.table.column("3", minwidth=40, stretch="no", anchor="center")
        self.table.heading("4", text="VALOR")
        self.table.column("4", minwidth=60, stretch="no", anchor="center")
        self.table.heading("5", text="VALIDADE")
        self.table.column("5", minwidth=90, stretch="no", anchor="center")
        self.table["show"] = "headings"
        self.table.pack(fill="both")
        
        #inserindo dados para teste na tabela
        self.table.insert(parent='', index=0, values=(1, "PÃO", 15, 20, "10-4-2025"))
        
        self.main_window.mainloop()
        
app=Read()

        
