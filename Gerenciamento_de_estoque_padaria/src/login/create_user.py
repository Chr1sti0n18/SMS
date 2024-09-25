from bd_login import Database
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image

class Create_user: 

    def __init__(self):
        self.bd = Database("bd_users.db")

        self.main_window = tk.Tk()
        self.main_window.title("Cadastro de Usuários")
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        self.main_window.geometry(f"{screen_width}x{screen_height}+0+0")
        self.main_window.state("zoomed")

        self.nome = ctk.StringVar()
        self.senha = ctk.StringVar()       
        self.nivel_acesso = ctk.StringVar()

        logo = ctk.CTkImage(light_image=Image.open("Gerenciamento_de_estoque_padaria/src/assets/logo.png"), 
                            dark_image=Image.open("Gerenciamento_de_estoque_padaria/src/assets/logo.png"), size=(90, 90))
        
        # Criando frame principal
        self.frame1 = ctk.CTkFrame(self.main_window)
        self.frame1.pack(side="top", fill="y", expand = False, ipadx = 1280)
        self.inner_frame1 = ctk.CTkFrame(self.frame1, fg_color="#FFC07E")
        self.inner_frame1.pack(fill="both") 

        self.head = ctk.CTkLabel(self.inner_frame1, text="Cadastro de usuários", font=("Segoe Script", 52, "bold"), 
                                 fg_color="#FFC07E", text_color="#554131",height=90, width=screen_width, anchor="center")
        
        self.image_label = ctk.CTkLabel(self.inner_frame1, image=logo, text="")
        self.image_label.pack(side="left", anchor="w")  # Sem padding, a imagem fica na extrema esquerda
        
        self.head.pack(fill="both")

        self.labelNome = ctk.CTkLabel(self.frame1, text="Nome do Usuário", fg_color="#535c68", font=ctk.CTkFont("CENTURY GOTHIC", 16), text_color="white")
        self.labelNome.pack(padx=10, pady=10)
        self.txt_Nome = ctk.CTkEntry(self.frame1, textvariable=self.nome, font=ctk.CTkFont("CENTURY GOTHIC", 16), width=30)
        self.txt_Nome.pack(padx=10, pady=10)

        self.labelSenha = ctk.CTkLabel(self.frame1, text="Senha", fg_color="#535c68", font=("CENTURY GOTHIC", 16), fg="white")
        self.labelSenha.pack(padx=10, pady=10)
        self.txt_Senha = ctk.CTkEntry(self.frame1, textvariable=self.senha, font=("CENTURY GOTHIC", 16), width=30, show="*")
        self.txt_Senha.pack(padx=10, pady=10)

        self.label_Nivel_acesso = ctk.CTkLabel(self.frame1, text="Cargo do Usuário", fg_color="#535c68", font=ctk.CTkFont("CENTURY GOTHIC", 16), text_color="white")
        self.label_Nivel_acesso.pack(padx=10, pady=10, sticky="w")
        self.txt_Nivel_acesso= ctk.CTkEntry(self.frame1, textvariable=self.nivel_acesso, font=("CENTURY GOTHIC", 16), width=30)
        self.txt_Nivel_acesso.pack(padx=10)

        
        self.frame2 = ctk.CTkFrame(self.frame1, fg_color="#535c68")
        self.frame2.pack(padx=10, pady=10)
    

        self.btnAdd = ctk.CTkButton(self.frame2, text="Adicionar", width=15, font=("CENTURY GOTHIC", 16, "bold"), text_color="white", fg_color="#16a085", command = self.inserir_funcionario)
        self.btnAdd.pack(padx=10)
    
        self.btnEdit = ctk.CTkButton(self.frame2, text="Editar", width=15, font=("CENTURY GOTHIC", 16, "bold"), text_color="white", fg_color="#2980b9", command = self.editar_funcionario)
        self.btnEdit.pack(padx=10)

        self.btnDel = ctk.CTkButton(self.frame2, text="Deletar", width=15, font=("CENTURY GOTHIC", 16, "bold"), text_color="white", fg_color="#16a085", command = self.del_funcionario)
        self.btnDel.pack(padx=10)

        self.btnClear = ctk.CTkButton(self.frame2,  text="Limpar Campos", width=15, font=("CENTURY GOTHIC", 16, "bold"), text_color="white", fg_color="#f39c12", command = self.clearAll)
        self.btnClear.pack(padx=10)
        

        self.frame3 = ctk.CTkFrame(self.main_window, fg_color="#ecf0f1", width=1980, height=520)
        self.frame3.place(x=0, y=250)


        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", font=("CENTURY GOTHIC, 18"), rowheight=50)
        self.style.configure("mystyle.Treeview", font=("CENTURY GOTHIC, 18"))
        self.tv = ttk.Treeview(self.frame3, columns =(1, 2, 3, 4, 5 ), style="mystyle.Treeview")
        self.tv.heading("1", text="ID")
        self.tv.column("1", width=40, stretch="no")
        self.tv.heading("2", text="Nome")
        self.tv.column("2", width=300, stretch="no")
        self.tv.heading("3", text="Senha")
        self.tv.column("3", width=60, stretch="no")
        self.tv.heading("4", text="Nível de acesso")
        self.tv.column("4", width=200, stretch="no")        
        self.tv["show"] = "headings"

        self.tv.bind("<ButtonRelease-1>", self.getData)
        self.tv.pack(fill="x")
        self.displayAll()
        self.main_window.mainloop()


    def getData(self, event):
        
        selected_row = self.tv.focus()            
        data = self.tv.item(selected_row)
        global row
        row = data["values"]
        
        self.txt_Nome.delete(0, "END")
        self.txt_Senha.delete(0, "END")
        self.txt_Nivel_acesso.delete(0, "END")
        
        
        self.txt_Nome.insert("END", row[1])
        self.txt_Senha.insert("END", row[2])
        self.txt_Nivel_acesso.insert("END", row[4])
        
        

    def displayAll(self):
        self.tv.delete(*self.tv.get_children())
        for row in self.bd.fetch():
            self.tv.insert("", "END", values=row)
            
    def clearAll(self):
        self.txt_Nome.delete(0, "END")
        self.txt_Senha.delete(0, "END")
        self.txt_Nivel_acesso.delete(0, "END")
        

    def inserir_funcionario(self):
        
        if (self.txt_Nome.get == "" or self.txt_Senha.get() == 0 or  self.txt_Nivel_acesso.get() == ""):
            messagebox.showerror("Erro na entrada", "Por favor preencha todos os campos")
        else:
            self.bd.insert(self.txt_Nome.get(), self.txt_Senha.get(), self.txt_Nivel_acesso.get())
            messagebox.showinfo("Sucesso", "Usuário cadastrado")
            self.clearAll()
            self.displayAll()
                  

    def editar_funcionario(self):
        
        if (self.txt_Nome.get == "" or self.txt_Senha.get() == 0 or  self.txt_Nivel_acesso.get() == ""):
            messagebox.showerror("Erro na entrada", "Por favor preencha todos os campos")
            
        else:
            self.bd.update(row[0], self.txt_Nome.get(), self.txt_Senha.get(), self.txt_Nivel_acesso.get())
            messagebox.showinfo("Sucesso", "Usuário Atualizado")
            self.clearAll()
            self.displayAll()

    def del_funcionario(self):
        self.bd.remove(row[0])
        messagebox.showinfo("Sucesso", "Usuário Excluído")
        self.clearAll()
        self.displayAll()

        self.main_window.mainloop()



Create_user()