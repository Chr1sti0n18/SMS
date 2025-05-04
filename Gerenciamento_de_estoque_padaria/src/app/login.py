from customtkinter import *
from customtkinter import CTkImage
from PIL import Image
from src import Data
from src import Read
from tkinter import messagebox
import os

# Caminho absoluto até o ícone
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ICON_PATH = os.path.join(BASE_DIR, '..', 'assets', 'logo_sem_fundo.ico')
LOGO_PATH = os.path.join(BASE_DIR, '..', 'assets', 'logo.png')

class Login():
    def __init__(self):
        # Definindo váriavel global para a janela principal
        self.db = Data("bd_users.db")
        rows = self.db.fetch()
        if not rows:
            from src import Manipulate
            Manipulate()
            return 0
        global username
        global password
        self.main_window = CTk()
        self.main_window.title("Login")
        altura = self.main_window.winfo_screenheight()
        largura = self.main_window.winfo_screenwidth()
        largura_janela = 640
        altura_janela = 480
        pos_x = (largura - largura_janela) // 2
        pos_y = (altura - altura_janela) // 2
        self.main_window.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
        self.main_window._set_appearance_mode("system")
        self.main_window.iconbitmap(ICON_PATH)
        self.main_window.resizable(False,False)   
        username = StringVar()
        password = StringVar()
        
        logo = CTkImage(light_image=Image.open(LOGO_PATH), 
                            dark_image=Image.open(LOGO_PATH), size=(90, 90))
        
        # Montando a estrutura da Tela
        title_label = CTkLabel(self.main_window,text="Qui Pães",fg_color="#FFC07E",text_color="#554131",
                            font=CTkFont(family="Segoe Script", size=52, weight="bold"),height=100, image=logo, compound="left", width=640)
        title_label.pack()

        login_frame = CTkFrame(self.main_window, fg_color="transparent")
        login_frame.pack(pady=20)
        
        user_label = CTkLabel(login_frame,font=("Segoe UI Light", 22, "bold"), text="Usuário")
        user_label.pack(anchor="s", pady=15)
        user_entry = CTkEntry(login_frame,font=("Segoe UI Light", 22), placeholder_text="Seu usuário", textvariable=username)
        user_entry.pack(padx=10)
        user_label = CTkLabel(login_frame,font=("Segoe UI Light", 22, "bold"), text="Senha")
        user_label.pack(anchor="s", pady=15)
        password_entry = CTkEntry(login_frame,bg_color="white",font=("Segoe UI Light", 22),show="*", textvariable=password)
        password_entry.pack(padx=10)

        self.btn_submit = CTkButton(login_frame,text="Login",font=("Segoe UI", 22, "bold"), fg_color='#554131', command=self.entering, hover_color="#87463f")
        self.btn_submit.pack(padx=10,pady=40)
        self.main_window.bind("<Return>", self.on_enter)

        self.main_window.mainloop()

    def on_enter(self, event=None):
        self.btn_submit.invoke()

    def entering(self):
        uname = username.get()
        pwd = password.get()

        if uname == "" or pwd == "":
            messagebox.showerror("Erro", "Ainda há campo(s) vazio(s)!")
        else:
            rows = self.db.logar(uname, pwd)
            print(rows)
            if rows:

                messagebox.showinfo("Sucesso!", "Login Realizado com sucesso!!")

                funcao = rows[3]

                if funcao == "Admin":
                    from src import App_menu
                    self.main_window.destroy()
                    tela_menu = App_menu()
                
                if funcao == "Padrão":
                    self.main_window.destroy()
                    tela_read = Read()

            else:
                messagebox.showerror("Erro", "Nome de usuário ou senha incorreto!")