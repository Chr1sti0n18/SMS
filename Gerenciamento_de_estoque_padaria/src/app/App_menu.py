import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from Read_products import *
from manipulate_user import *

class App_menu:
    def __init__(self):
        global main_window
        main_window = tk.Tk()
        main_window.title("Menu")
        main_window.state("zoomed")
        main_window.iconbitmap('Gerenciamento_de_estoque_padaria/src/assets/logo_sem_fundo.ico')
        screen_width = main_window.winfo_width()
        screen_height = main_window.winfo_height()
        self.frame1 = ctk.CTkFrame(main_window)
        self.frame1.pack(side="top", fill="y", expand = False, ipadx = 1280)


        
        # Texto do inner frame
        self.head = ctk.CTkLabel(self.frame1, text="Menu", font=("Segoe Script", 52, "bold"), 
                                 fg_color="#FFC07E", text_color="#554131", height=120, width=screen_width, anchor="center")
        self.head.pack(fill="both")

        self.frame_buttons = ctk.CTkFrame(main_window, fg_color="transparent", width=screen_width)
        self.frame_buttons.pack(anchor="se", fill="both")
        self.imagem_pao = Image.open("Gerenciamento_de_estoque_padaria/src/assets/pão.png")  
        self.imagem_pao = self.imagem_pao.resize((475, 900))
        self.imagem_tk = ImageTk.PhotoImage(self.imagem_pao)
        self.product_button = tk.Button(master= self.frame_buttons, image=self.imagem_tk, text="Gerenciar Produtos", compound="center", width=475, height=900, font=("Segoe Script", 30, "bold"), fg="#FFF", command=self.call_read)
        self.product_button.pack(side="left")
        self.imagem_func = Image.open("Gerenciamento_de_estoque_padaria/src/assets/func_padaria.png")  
        self.imagem_func = self.imagem_func.resize((475, 900))
        self.imagem_funcTk = ImageTk.PhotoImage(self.imagem_func)
        self.users_button = tk.Button(self.frame_buttons, image=self.imagem_funcTk, text="Gerenciar Usuários", compound="center", width=475, height=900, font=("Segoe Script", 30, "bold"), fg="#FFF", command=self.call_users)
        self.users_button.pack(side="left")
        main_window.mainloop()
    
    def call_users(self):
        main_window.destroy()
        Manipulate()

    def call_read(self):
        main_window.destroy()
        Read()