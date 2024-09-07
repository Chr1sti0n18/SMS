from tkinter import *
import customtkinter as ctk
from PIL import Image

class Create:

    def __init__(self):

        self.main_window = ctk.CTk()
        self.main_window.title("Cadastro de Produto")
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        self.main_window.geometry(f"{screen_width}x{screen_height}+0+0")
        
        logo = ctk.CTkImage(light_image=Image.open("Gerenciamento_de_estoque_padaria/src/assets/logo.png"), 
                            dark_image=Image.open("Gerenciamento_de_estoque_padaria/src/assets/logo.png"), size=(90, 90))    
        
        # Criando frame principal
        self.frame1 = ctk.CTkFrame(self.main_window)
        self.frame1.pack(side="top", fill="y", expand = False, ipadx = 1280)
        self.inner_frame1 = ctk.CTkFrame(self.frame1)
        self.inner_frame1.pack(fill="both") 
        
         # Texto da frame principal
        self.head = ctk.CTkLabel(self.inner_frame1, text="Cadastro de produtos", font=ctk.CTkFont(family="montserrat", size=22, weight="bold"), 
                                 fg_color="#FFC07E", text_color="#554131",height=90, width=screen_width, anchor="center")
        
        self.image_label = ctk.CTkLabel(self.inner_frame1, image=logo, text="")
        self.image_label.pack(side="left", anchor="w")  # Sem padding, a imagem fica na extrema esquerda
        
        self.head.pack(fill="both") 

        #Criando o formulário de criação de produto
        self.frame_form = ctk.CTkFrame(self.main_window)
        self.frame_form.pack(fill="y")
        self.form_codigo = ctk.CTkEntry(self.frame_form, placeholder_text="Insira ou escaneie o código")
        self.form_codigo.pack(side="left")

        self.main_window.mainloop()

create = Create()