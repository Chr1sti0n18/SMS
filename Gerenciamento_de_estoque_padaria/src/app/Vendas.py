import customtkinter as ctk
import tkinter as tk
from tkinter import END, ttk
from tkinter import messagebox
from PIL import Image
import os

class Vendas: 

    def __init__(self):
        from src import Data2
        self.db = Data2("vendas.db")

        self.main_window = tk.Tk()
        self.main_window.title("Cadastro de vendas")
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        self.main_window.geometry(f"{screen_width}x{screen_height}+0+0")
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        ICON_PATH = os.path.join(BASE_DIR, '..', 'assets', 'logo_sem_fundo.ico')
        self.main_window.iconbitmap(ICON_PATH)
        self.main_window.state("zoomed")
        
        LOGO_PATH = os.path.join(BASE_DIR, '..', 'assets', 'logotipo.png')
        logo = ctk.CTkImage(light_image=Image.open(LOGO_PATH), 
                            dark_image=Image.open(LOGO_PATH), size=(90,90))  
        
        # Criando frame principal
        self.inner_frame1 = ctk.CTkFrame(self.main_window, fg_color="#FFC07E")
        self.inner_frame1.pack(fill="y", expand = False, side="top", ipadx=1280) 
        self.frame1 = ctk.CTkFrame(self.main_window, fg_color="transparent")
        self.frame1.pack(side="top", fill="y", expand = False, ipadx = 1280, ipady=30)

        self.head = ctk.CTkLabel(self.inner_frame1, text="Cadastro de vendas", font=("Segoe Script", 52, "bold"), 
                                 fg_color="#FFC07E", text_color="#554131",height=90, width=screen_width, anchor="center")
        
        self.image_label = ctk.CTkLabel(self.inner_frame1, image=logo, text="")
        self.image_label.pack(side="left", anchor="w")  # Sem padding, a imagem fica na extrema esquerda
        
        self.head.pack(fill="both", pady=40)
   
        self.frame2 = ctk.CTkFrame(self.frame1, fg_color="transparent")
        self.frame2.pack(padx=10, pady=25)
    

        self.btnAdd = ctk.CTkButton(self.frame2, text="Iniciar", width=15, font=ctk.CTkFont("Segoe UI", 18, "bold"), text_color="white", fg_color="#16a085", command = self.inserir_venda)
        self.btnAdd.pack(padx=10, pady=10)
    
        self.btnEdit = ctk.CTkButton(self.frame2, text="Atualizar", width=15, font=ctk.CTkFont("Segoe UI", 18, "bold"), text_color="white", fg_color="#2980b9", command = self.displayAll)
        self.btnEdit.pack(padx=10, pady=10)

        self.btnDel = ctk.CTkButton(self.frame2, text="Deletar", width=15, font=ctk.CTkFont("Segoe UI", 18, "bold"), text_color="white", fg_color="crimson", command = self.del_venda)
        self.btnDel.pack(padx=10, pady=10)


        self.frame3 = ctk.CTkFrame(self.main_window, fg_color="transparent", width=1980, height=520)
        self.frame3.pack()


        self.table_frame=ctk.CTkFrame(self.frame3)
        self.table_frame.pack(anchor="center", pady=15)
        self.table_style=ttk.Style()
        self.table_style.configure("Treeview", rowheight=20, fieldbackground='#EBEBEB', 
                                   font=ctk.CTkFont("Segoe UI", 18, 'bold'))
        self.table_style.configure("Heading", font=ctk.CTkFont(family="Segoe UI", size=18, weight='bold'))
        self.table_style.map('Treeview', background=[('selected', 'grey')])
        self.table=ttk.Treeview(self.table_frame, columns=(1, 2, 3, 4, 5, 6))
        
        # Criando as colunas da tabela
        self.table.heading("1", text="ID")
        self.table.column("1", width=180, stretch="no", anchor="center")
        self.table.heading("2", text="IDPRODUTO")
        self.table.column("2", minwidth=120, stretch="no", anchor="center")
        self.table.heading("3", text="PRODUTO")
        self.table.column("3", minwidth=60, stretch="no", anchor="center")
        self.table.heading("4", text="DATA")
        self.table.column("4", minwidth=60, stretch="no", anchor="center")
        self.table.heading("5", text="QUANTIDADE")
        self.table.column("5", minwidth=60, stretch="no", anchor="center")
        self.table.heading("6", text="VALOR TOTAL")
        self.table.column("6", minwidth=60, stretch="no", anchor="center")
        self.table["show"] = "headings"
        self.table.pack(fill="both")

        self.table.bind("<ButtonRelease-1>", self.pegar_dados)
        self.displayAll()
        self.main_window.mainloop()


    def pegar_dados(self, event):
        global selected_item 
        selected_item = self.table.focus()
        data = self.table.item(selected_item)
        global row
        row = data["values"]
        
    def displayAll(self):
        self.table.delete(*self.table.get_children())
        for row in self.db.fetch():
            self.table.insert("", END, values=row)
            
    def inserir_venda(self):
        from src import GetProduto
        GetProduto()

    def del_venda(self):
        self.db.remove(row[0])
        messagebox.showinfo("Sucesso", "Venda Excluída")
        self.clearAll()
        self.displayAll()
