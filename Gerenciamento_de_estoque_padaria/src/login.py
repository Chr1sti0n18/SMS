from tkinter import *

def Login():
    # criar a lógica de Login
    ""

def LoginForm():

    global main_window
    main_window = Tk()
    main_window.title("Login")
    main_window.geometry("640x480+620+275")
    main_window["bg"] = "#EBEBEB"
    main_window.resizable(False,False)   

    #Montando a estrutura da Tela
    title_label = Label(main_window,text="Ki Pães",bg="#756645",fg="#F4EE82",
                        font=("Montserrat", 52, "bold"),justify=CENTER,padx=200)
    title_label.place(x=0,y=0,height=100)
    user_label = Label(main_window,text="Usuário",bg="#EBEBEB",fg="#000",font=("Montserrat", 22, "bold"))
    user_label.place(x=60,y=175)
    user_entry = Entry(main_window,bg="white",fg="black",font=("Montserrat", 22))
    user_entry.place(x=190,y=175)
    password_label = Label(main_window,text="Senha",bg="#EBEBEB",fg="#000",font=("Montserrat", 22, "bold"))
    password_label.place(x=80,y=260)
    password_entry = Entry(main_window,bg="white",fg="black",font=("Montserrat", 22),show="*")
    password_entry.place(x=190,y=260)

    btn_submit = Button(main_window,bg="#00FF00",text="Entrar",fg="#000",width=10,height=1,font=("Montserrat", 22, "bold"),border=3,activebackground="#7CFC00")
    btn_submit.place(x=220,y=350)

    main_window.mainloop()

LoginForm()