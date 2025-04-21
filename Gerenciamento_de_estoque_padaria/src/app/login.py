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

def Login():
    db = Data("bd_users.db")

    uname = username.get()
    pwd = password.get()

    if uname == "" or pwd == "":
        messagebox.showerror("Erro", "Ainda há campo(s) vazio(s)!")
    else:
        rows = db.logar(uname, pwd)
        print(rows)
        if rows:

            messagebox.showinfo("Sucesso!", "Login Realizado com sucesso!!")

            funcao = rows[3]

            if funcao == "Admin":
                from src import App_menu
                main_window.destroy()
                tela_menu = App_menu()
            
            if funcao == "Padrão":
                main_window.destroy()
                tela_read = Read()

        else:
            messagebox.showerror("Erro", "Nome de usuário ou senha incorreto!")

def LoginForm():
    # Definindo váriavel global para a janela principal
    global username
    global password
    global main_window
    main_window = CTk()
    main_window.title("Login")
    main_window.geometry("640x480+620+275")
    main_window._set_appearance_mode("system")
    main_window.iconbitmap(ICON_PATH)
    main_window.resizable(False,False)   
    username = StringVar()
    password = StringVar()
    
    logo = CTkImage(light_image=Image.open(LOGO_PATH), 
                        dark_image=Image.open(LOGO_PATH), size=(90, 90))
    
    # Montando a estrutura da Tela
    title_label = CTkLabel(main_window,text="Qui Pães",fg_color="#FFC07E",text_color="#554131",
                        font=CTkFont(family="Segoe Script", size=52, weight="bold"),height=100, image=logo, compound="left", width=640)
    title_label.pack()

    login_frame = CTkFrame(main_window, fg_color="transparent")
    login_frame.pack(pady=20)
    
    user_label = CTkLabel(login_frame,font=("Segoe UI Light", 22, "bold"), text="Usuário")
    user_label.pack(anchor="s", pady=15)
    user_entry = CTkEntry(login_frame,font=("Segoe UI Light", 22), placeholder_text="Seu usuário", textvariable=username)
    user_entry.pack(padx=10)
    user_label = CTkLabel(login_frame,font=("Segoe UI Light", 22, "bold"), text="Senha")
    user_label.pack(anchor="s", pady=15)
    password_entry = CTkEntry(login_frame,bg_color="white",font=("Segoe UI Light", 22),show="*", textvariable=password)
    password_entry.pack(padx=10)

    btn_submit = CTkButton(login_frame,text="Login",font=("Segoe UI", 22, "bold"), fg_color='#554131', command=Login, hover_color="#87463f")
    btn_submit.pack(padx=10,pady=40)

    main_window.mainloop()

LoginForm()