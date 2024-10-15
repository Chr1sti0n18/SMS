import tkinter as tk
from tkinter import END, ttk
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from dbProducts import Database

class DeletarProduto:
    def __init__(self):
        self.db = Database("products.db")

        self.main_window = tk.Tk()
        screen_width = self.main_window.winfo_screenwidth()
        screen_height = self.main_window.winfo_screenheight()
        self.main_window.title("Deletar")
        self.main_window.geometry(f"{screen_width}x{screen_height}+0+0")
        self.main_window.resizable(False, False)
        self.main_window.state("zoomed")

        # Carregando a logo
        logo = ctk.CTkImage(light_image=Image.open("Gerenciamento_de_estoque_padaria/src/assets/logo.png"), 
                            dark_image=Image.open("Gerenciamento_de_estoque_padaria/src/assets/logo.png"), size=(90, 90))    
        
        # Criando frame principal
        self.frame1 = ctk.CTkFrame(self.main_window)
        self.frame1.pack(side="top", fill="y", expand = False, ipadx = 1280)
        
        self.inner_frame2 = ctk.CTkFrame(self.main_window)
        self.inner_frame2.configure(fg_color='transparent')
        self.inner_frame2.pack(fill='both', ipadx=305, pady=10)
        # Criando inner frame 
        self.inner_frame1 = ctk.CTkFrame(self.frame1)
        self.inner_frame1.pack(fill="y", expand=False, side="top", ipadx=1280) 

        self.frame2 = ctk.CTkFrame(self.main_window, fg_color="transparent")
        self.frame2.pack()

        
        # Texto do inner frame
        self.head = ctk.CTkLabel(self.inner_frame1, text="Deletar Produto", font=("Segoe Script", 52, "bold"), 
                                 fg_color="#FFC07E", text_color="#554131", height=120, width=screen_width, anchor="center")
        
        #posicionando logo 
        self.image_label = ctk.CTkLabel(self.inner_frame1, image=logo, text="")
        self.image_label.pack(side="left", anchor="w")  
        
        self.head.pack(fill="both") 


        self.combobox = ctk.CTkComboBox(self.inner_frame2, values=["Todos", "Salgados", "Enlatados", "Doces"], 
                                        corner_radius=15, width=150, font=ctk.CTkFont(family="Segoe UI"), command=self.teste)
        self.combobox.pack(side='right', padx=205)

        # Criando a tabela de produtos
        self.table_frame=ctk.CTkFrame(self.frame2, bg_color="white")
        self.table_frame.pack(anchor="center", pady=15)
        self.table_style=ttk.Style()
        self.table_style.configure("Treeview", background="#EBEBEB", rowheight=20, fieldbackground='#EBEBEB', 
                                   font=ctk.CTkFont(family="Segoe UI", size=10))
        self.table_style.configure("Heading", font=ctk.CTkFont(family="Segoe UI", size=10))
        self.table_style.map('Treeview', background=[('selected', 'grey')])
        self.table=ttk.Treeview(self.table_frame, columns=(1, 2, 3, 4, 5, 6))
        
        # Criando as colunas da tabela
        self.table.heading("1", text="ID")
        self.table.column("1", width=180, stretch="no", anchor="center")
        self.table.heading("2", text="PRODUTO")
        self.table.column("2", minwidth=120, stretch="no", anchor="center")
        self.table.heading("3", text="QUANTIDADE")
        self.table.column("3", minwidth=40, stretch="no", anchor="center")
        self.table.heading("4", text="PRECO")
        self.table.column("4", minwidth=60, stretch="no", anchor="center")
        self.table.heading("5", text="VALIDADE")
        self.table.column("5", minwidth=90, stretch="no", anchor="center")
        self.table.heading("6", text="Categoria")
        self.table.column("6", minwidth=90, stretch="no", anchor="center")
        self.table["show"] = "headings"
        self.table.pack(fill="both")
        self.displayAll()

        #botão para deletar o produto selecionado
        self.botao_deletar = ctk.CTkButton(self.frame2, text="Deletar Produto Selecionado", 
                                           command=self.deletar_produto, fg_color="#554131", 
                                           text_color="#EBEBEB", width=150, font=ctk.CTkFont("Segoe UI", 16, "bold"))
        self.botao_deletar.pack(pady=100)

        self.main_window.mainloop()

    def deletar_produto(self):
        # Obtém o item selecionado
        selected_item = self.table.selection()

        if not selected_item:
            messagebox.showwarning("Aviso", "Nenhum produto selecionado!")
            return

        # Pega os valores do item selecionado
        produto_selecionado = self.table.item(selected_item, "values")

        # Confirmação
        confirmacao = messagebox.askquestion("Confirmação", f"Tem certeza que deseja deletar o produto {produto_selecionado[1]}?")
        
        if confirmacao == 'yes':
            # Deleta o produto da tabela
            self.table.delete(selected_item)
            messagebox.showinfo("Sucesso", f"Produto '{produto_selecionado[1]}' deletado com sucesso.")
        else:
            messagebox.showinfo("Cancelado", "Exclusão do produto cancelada.")
    
    def teste (self, choice):
        self.table.delete(*self.table.get_children())
        for row in self.db.fetch(choice):
            self.table.insert("", END, values = row)
        
    def displayAll(self):
        filter = self.combobox.get()
        self.table.delete(*self.table.get_children())
        for row in self.db.fetch(filter):
            self.table.insert("", END, values = row)


app = DeletarProduto()