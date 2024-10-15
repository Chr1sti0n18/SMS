import customtkinter as ctk
import tkinter as tk
from PIL import Image

class Update:

    def __init__(self):

        self.main_window = tk.Tk()
        self.main_window.title("Atualização de Produto")
        screen_width = self.main_window.winfo_screenwidth()
        self.main_window.state("zoomed")

        logo = ctk.CTkImage(light_image=Image.open("Gerenciamento_de_estoque_padaria/src/assets/logotipo.png"), 
                            dark_image=Image.open("Gerenciamento_de_estoque_padaria/src/assets/logotipo.png"), size=(120, 120))

        self.frame1 = ctk.CTkFrame(self.main_window)
        self.frame1.configure(fg_color='transparent')
        self.frame1.pack(side="top", fill="y", expand = False, ipadx = 1280)

        self.inner_frame1 = ctk.CTkFrame(self.frame1, fg_color="#FFC07E")
        self.inner_frame1.configure(fg_color='#EBEBEB')
        self.inner_frame1.pack(fill="both") 

        self.head = ctk.CTkLabel(self.inner_frame1, text="Atualização de Produtos", font=ctk.CTkFont(family="Segoe Script", size=52, weight="bold"), 
                                 fg_color="#FFC07E", text_color="#554131",height=120, width=screen_width, anchor="center")
        
        # Posicionando logo no head da aba
        self.image_label = ctk.CTkLabel(self.inner_frame1, image=logo, text='')
        self.image_label.pack(side="left", anchor="w")  # Sem padding, a imagem fica na extrema esquerda
        self.head.pack(fill="both", anchor='center')

        self.main_window.mainloop()


Update()