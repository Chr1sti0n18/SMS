from customtkinter import *

def Login():
    # criar a lógica de Login
    ""

def LoginForm():
    # Definindo váriavel global para a janela principal
    global main_window
    main_window = CTk()
    main_window.title("Login")
    main_window.geometry("640x480+620+275")
    main_window._set_appearance_mode("system")
    main_window.resizable(False,False)   

    # Montando a estrutura da Tela
    title_label = CTkLabel(main_window,text="Ki Pães",bg_color="#756645",text_color="#F4EE82",
                        font=("Montserrat", 52, "bold"),padx=400,height=100)
    title_label.pack()
    user_entry = CTkEntry(main_window,bg_color="white",font=("Montserrat", 22),placeholder_text="Seu usuário")
    user_entry.pack(padx=10,pady=60)
    password_entry = CTkEntry(main_window,bg_color="white",font=("Montserrat", 22),show="*",placeholder_text="Sua senha")
    password_entry.pack(padx=10)

    btn_submit = CTkButton(main_window,text="Login",font=("Montserrat", 22, "bold"))
    btn_submit.pack(padx=10,pady=60)

    main_window.mainloop()

LoginForm()