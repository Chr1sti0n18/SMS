import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

class Read:
    def __init__(self):
        # Criando a estrutura da janela
        self.main_window = ctk.CTk()
        self.main_window.title("Produtos")
        self.main_window.geometry("1280x720+0+0")
        self.main_window.configure(fg_color="#EBEBEB")
        self.main_window.state("zoomed")  
        
        self.frame1 = ctk.CTkFrame(self.main_window)
        self.frame1.pack(side="top", fill="y", expand = False, ipadx = 1280)
        
        self.head = ctk.CTkLabel(self.frame1, text="Produtos", font=("MONTSERRAT", 22, "bold"), fg_color="#756645", text_color="#F4EE82",height=48)
        self.head.pack(fill="both") 
        # Criando a tabela
        self.table_frame=ctk.CTkFrame(self.main_window, bg_color="white")
        self.table_frame.pack(anchor="center", pady=25)
        self.table_style=ttk.Style()
        self.table=ttk.Treeview(self.table_frame, columns=(1, 2, 3, 4, 5))
        
        self.table.heading("1", text="ID")
        self.table.column("1", width=60, stretch="no", anchor="center")
        self.table.heading("2", text="PRODUTO")
        self.table.column("2", minwidth=120, stretch="no", anchor="center")
        self.table.heading("3", text="QUANT")
        self.table.column("3", minwidth=40, stretch="no", anchor="center")
        self.table.heading("4", text="VALOR")
        self.table.column("4", minwidth=60, stretch="no", anchor="center")
        self.table.heading("5", text="VALIDADE")
        self.table.column("5", minwidth=90, stretch="no", anchor="center")
        self.table["show"] = "headings"
        self.table.pack(fill="both")
        #inserindo dados para teste na tabela
        self.table.insert(parent='', index=0, values=(1, "PÃO", 15, 20, "10-4-2025"))
        
        self.main_window.mainloop()
        
app=Read()

        
