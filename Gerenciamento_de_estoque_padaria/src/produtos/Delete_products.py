import tkinter as tk
from tkinter import messagebox  # Importação explícita do messagebox
import customtkinter as ctk

class Delete:
    def __init__(self):
        # Janela principal
        self.janela_principal = ctk.CTk()
        self.janela_principal.title("Deletar Produto")
        self.janela_principal.geometry("1280x720+0+0") 
        self.janela_principal.configure(fg_color="#EBEBEB")

        # Cria o frame principal para o conteúdo
        self.frame1 = ctk.CTkFrame(self.janela_principal)
        self.frame1.pack(side="top", fill="y", expand=True)

        # Cabeçalho
        self.cabecalho = ctk.CTkLabel(self.frame1, text="Deletar Produto", font=("MONTSERRAT", 22, "bold"),
                                      fg_color="#FFC07E", text_color="#554131", height=80, compound="left", padx=1280)
        self.cabecalho.pack(fill="x")
        
        # Confirmação da exclusão
        self.botao_deletar = ctk.CTkButton(self.frame1, text="Deletar Produto", command=self.deletar_produto)
        self.botao_deletar.pack(pady=20)

        self.janela_principal.mainloop()

    def deletar_produto(self):
        mensagem = messagebox.askquestion("Confirmação", "Tem certeza que deseja deletar este produto?")
        if mensagem == 'yes':  # Corrigido para 'yes' em vez de 'sim' (para compatibilidade com tkinter)
            print("Produto deletado")  
            messagebox.showinfo("Sucesso", "Produto deletado com sucesso.")
        else:
            messagebox.showinfo("Cancelado", "Exclusão do produto cancelada.")

app = Delete()