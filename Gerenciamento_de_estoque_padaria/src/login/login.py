from customtkinter import *
from customtkinter import CTkImage
from PIL import Image
from bd_login import Database

def Login():
    db = Database("bd_users.db")

    uname = username.get()
    pwd = password.get()

    if uname == "" or pwd == "":
        message.set("Preencha")

def LoginForm():
    # Definindo váriavel global para a janela principal
    global username
    global password
    global message
    username = StringVar()
    password = StringVar()
    message = StringVar()
    global main_window
    main_window = CTk()
    main_window.title("Login")
    main_window.geometry("640x480+620+275")
    main_window._set_appearance_mode("system")
    main_window.resizable(False,False)   
    
    logo = CTkImage(light_image=Image.open("src/assets/logo.png"), 
                        dark_image=Image.open("src/assets/logo.png"), size=(90, 90))
    
    # Montando a estrutura da Tela
    title_label = CTkLabel(main_window,text="Qui Pães",fg_color="#FFC07E",text_color="#554131",
                        font=CTkFont(family="Segoe Script", size=52, weight="bold"),height=100, image=logo, compound="left", width=640)
    title_label.pack()
    user_entry = CTkEntry(main_window,bg_color="white",font=("Segoe UI Light", 22),placeholder_text="Seu usuário")
    user_entry.pack(padx=10,pady=60)
    password_entry = CTkEntry(main_window,bg_color="white",font=("Segoe UI Light", 22),show="*",placeholder_text="Sua senha")
    password_entry.pack(padx=10)

    btn_submit = CTkButton(main_window,text="Login",font=("Segoe UI", 22, "bold"), command=Login)
    btn_submit.pack(padx=10,pady=60)

    main_window.mainloop()

LoginForm()