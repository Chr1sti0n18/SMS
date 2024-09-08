from tkinter import *
import customtkinter as ctk
from PIL import Image
from Read_products import Read
from Delete_products import Delete

class Create:

    def __init__(self):

        self.main_window = Tk()
        self.main_window.title("Cadastro de Produto")
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        self.main_window.geometry(f"{screen_width}x{screen_height}+0+0")
        self.main_window.state("zoomed")
        
        
        logo = ctk.CTkImage(light_image=Image.open("Gerenciamento_de_estoque_padaria/src/assets/logo.png"), 
                            dark_image=Image.open("Gerenciamento_de_estoque_padaria/src/assets/logo.png"), size=(90, 90))    
        
        # Criando frame principal
        self.frame1 = ctk.CTkFrame(self.main_window)
        self.frame1.pack(side="top", fill="y", expand = False, ipadx = 1280)
        self.inner_frame1 = ctk.CTkFrame(self.frame1, fg_color="#FFC07E")
        self.inner_frame1.pack(fill="both") 
        self.option_menu = ctk.CTkOptionMenu(self.inner_frame1, values=["Home", "Produtos", "Criação de Produtos"], fg_color="#EBEBEB", dropdown_fg_color="#EBEBEB", button_color="#EBEBEB", text_color="#554131",button_hover_color="#EBEBEB", font=ctk.CTkFont(family="Segoe UI", weight="bold"))
        self.option_menu.pack(side="right", anchor="w", padx=10, expand=False)

         # Texto da frame principal
        self.head = ctk.CTkLabel(self.inner_frame1, text="Cadastro de produtos", font=ctk.CTkFont(family="Segoe Script", size=52, weight="bold"), 
                                 fg_color="#FFC07E", text_color="#554131",height=90, width=screen_width, anchor="center")
        
        self.image_label = ctk.CTkLabel(self.inner_frame1, image=logo, text="")
        self.image_label.pack(side="left", anchor="w")  # Sem padding, a imagem fica na extrema esquerda
        
        self.head.pack(fill="both") 

        #Criando o formulário de criação de produto
        self.frame_form = ctk.CTkFrame(self.main_window)
        self.frame_form.pack(fill="both", expand=True)
        self.inner_frame_form = ctk.CTkFrame(self.frame_form)
        self.inner_frame_form.pack(ipadx=200, ipady=250, expand=True)
        self.form_codigo = ctk.CTkEntry(self.inner_frame_form, placeholder_text="Id do produto", height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_codigo.grid(row=0, column=1 , pady=50, padx=30)
        self.form_codigo = ctk.CTkEntry(self.inner_frame_form, placeholder_text="Nome", height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_codigo.grid(row=0, column=2, pady=50, padx=30)
        self.form_codigo = ctk.CTkEntry(self.inner_frame_form, placeholder_text="Preço", height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_codigo.grid(row=0, column=3, pady=50, padx=30)
        self.form_codigo = ctk.CTkEntry(self.inner_frame_form, placeholder_text="Quantidade", height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_codigo.grid(row=1, column=1, pady=50, padx=30)
        self.form_codigo = ctk.CTkEntry(self.inner_frame_form, placeholder_text="Validade", height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_codigo.grid(row=1, column=2, pady=50, padx=30)

        self.submit_button = ctk.CTkButton(self.inner_frame_form, text="Cadastrar", height=40, width=200, corner_radius=15)
        self.submit_button.grid(row=2, column=1, rowspan=2, columnspan=3, pady=20)
        

        self.main_window.mainloop()

create = Create()
