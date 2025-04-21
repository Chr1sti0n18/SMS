import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from Products import *
from manipulate_user import *
from Vendas import Vendas

class App_menu:
    def __init__(self):
        global main_window
        main_window = tk.Tk()
        main_window.title("Menu")
        main_window.state("zoomed")
        main_window.iconbitmap('Gerenciamento_de_estoque_padaria/src/assets/logo_sem_fundo.ico')
        screen_width = main_window.winfo_width()
        self.frame1 = ctk.CTkFrame(main_window, fg_color="#FFF")
        self.frame1.pack(side="top", fill="y", expand = False, ipadx = 1280)
        main_window.resizable(False, FALSE)
        main_window.iconbitmap('Gerenciamento_de_estoque_padaria/src/assets/logo_sem_fundo.ico')

        logo = ctk.CTkImage(light_image=Image.open("Gerenciamento_de_estoque_padaria/src/assets/logotipo.png"), 
                            dark_image=Image.open("Gerenciamento_de_estoque_padaria/src/assets/logotipo.png"), size=(200, 200))

        
        # Texto do inner frame
        self.head = ctk.CTkLabel(self.frame1, text="Menu", font=("Segoe Script", 52, "bold"), 
                                 fg_color="#FFC07E", text_color="#554131", height=120, width=screen_width, anchor="center")
        self.head.pack(fill="both")
        
        self.logoLabel=ctk.CTkLabel(main_window, image = logo, text = "")
        self.logoLabel.place(relx = 0.06, rely = 0.06, anchor = "center")

        self.frame_buttons = ctk.CTkFrame(main_window, fg_color="#FFF", width=screen_width, bg_color="#FFF")
        self.frame_buttons.pack(anchor="se", fill="both")
        self.imagem_pao = Image.open("Gerenciamento_de_estoque_padaria/src/assets/pão.png")  
        self.imagem_pao = self.imagem_pao.resize((400, 400))
        self.imagem_tk = ImageTk.PhotoImage(self.imagem_pao)
        self.product_button = tk.Button(master= self.frame_buttons, image=self.imagem_tk, compound="center", width=650, height=800, fg="#FFF", command=self.call_read, background="#f6f6f6")
        self.product_button.pack(side="left")
        self.imagem_func = Image.open("Gerenciamento_de_estoque_padaria/src/assets/func_padaria.png")
        self.imagem_func = self.imagem_func.resize((400, 400))
        self.imagem_funcTk = ImageTk.PhotoImage(self.imagem_func)
        self.users_button = tk.Button(self.frame_buttons, image=self.imagem_funcTk, compound="center", width=650, height=800, fg="#FFF", command=self.call_users, background="#f6f6f6")
        self.users_button.pack(side="left")
        self.imagem_vendas = Image.open("Gerenciamento_de_estoque_padaria/src/assets/vendas.png")
        self.imagem_vendas = self.imagem_vendas.resize((400, 400))
        self.imagem_vendasTk = ImageTk.PhotoImage(self.imagem_vendas)
        self.vendas_button = tk.Button(self.frame_buttons, image=self.imagem_vendasTk, compound="center", width=650, height=800, fg="#FFF", command=self.call_vendas, background="#f6f6f6")
        self.vendas_button.pack(side="left")
        
        self.bottom = ctk.CTkFrame(main_window,
                                 fg_color="#FFC07E", height=450, width=screen_width)
        self.bottom.pack()
        
        self.produtos = ctk.CTkLabel(self.frame_buttons, text="Gerenciar Estoque", font=("Segoe Script", 52, "bold"), 
                                 fg_color="#f6f6f6", text_color="#554131", height=120, width=screen_width*0.30)
        self.produtos.place(relx=0.16, rely=0.85, anchor="center")
        
        self.users = ctk.CTkLabel(self.frame_buttons, text="Gerenciar Usuários" , font=("Segoe Script", 52, "bold"), 
                                  fg_color="#f6f6f6", text_color="#554131", height=120, width=screen_width*0.30)
        self.users.place(relx=0.5, rely=0.85, anchor="center")
        
        self.vendas = ctk.CTkLabel(self.frame_buttons, text="Gerenciar Vendas" , font=("Segoe Script", 52, "bold"), 
                                 fg_color="#f6f6f6", text_color="#554131", height=120, width=screen_width*0.30)
        self.vendas.place(relx=0.84, rely=0.85, anchor="center")
        
        main_window.mainloop()
        
       
    
    def call_users(self):
        main_window.destroy()
        Manipulate()

    def call_read(self):
        main_window.destroy()
        Read()
        
    def call_vendas(self):
        main_window.destroy()
        Vendas()
         
App_menu()