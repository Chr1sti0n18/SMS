from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import os

class GetProduto:

    def __init__(self, callback=None):
        self.callback = callback
        #Conexões bancos de dados
        from src import Database
        self.db = Database ("products.db")
        from src import Data2
        self.dbVendas =  Data2 ("vendas.db")
        
        global main_window

        #Criação janela principal
        main_window = Tk()
        main_window.title("Cadastro de Vendas")
        main_window.resizable(False, FALSE)
       
        #Tamanho da janela
        self.screen_width = main_window.winfo_screenwidth()
        self.screen_height = main_window.winfo_screenheight()
        self.width=450
        self.height=350
        self.x = (self.screen_width // 2) - (self.width // 2)
        self.y = (self.screen_height // 2) - (self.height // 2)
        main_window.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        ICON_PATH = os.path.join(BASE_DIR, '..', 'assets', 'logo_sem_fundo.ico')
        main_window.iconbitmap(ICON_PATH)
        main_window.config(background='#EBEBEB') 
        
        # Criando frame principal
        self.frame1 = ctk.CTkFrame(main_window, fg_color='#EBEBEB')
        self.frame1.pack(side="top", fill="y", expand = False, ipadx = 500)
        self.inner_frame1 = ctk.CTkFrame(self.frame1, fg_color="#FFC07E")
        self.inner_frame1.pack(fill="both") 

         # Texto da frame principal
        self.head = ctk.CTkLabel(self.inner_frame1, text="$ Iniciar Venda $", font=ctk.CTkFont(family="Segoe Script", size=35, weight="bold"), 
                                 fg_color="#FFC07E", text_color="#554131",height=75, anchor="center")
        
        self.head.pack(fill="both") 

        #Expansão de tela, elementos na primeira tela estão abaixo da função
        def segundaTela():
            #Testes erros
            produto = self.db.searchID(self.form_id.get())
            if(self.form_id.get() == ""):
                    main_window.destroy()
                    return messagebox.showinfo("Erro", "Campo de ID vazio!") & main_window.mainloop()
            if(self.form_qtd.get() == "" or int(self.form_qtd.get()) < 1 or self.form_qtd.get() == None):
                    main_window.destroy()
                    return messagebox.showinfo("Erro", "Quantidade inválida!") & main_window.mainloop()
            if(int(self.form_qtd.get()) > int(produto[2])):
                    main_window.destroy()
                    return messagebox.showinfo("Erro", "Quantidade maior que a disponível em estoque!") & self.main_window.mainloop()    
            self.qtdProd = int(produto[2])
            #Dados do produto
            try:
                if(produto == None):
                     return  messagebox.showinfo("Erro", "Produto não encontrado")
            except Exception as e:
                main_window.destroy()
                return  messagebox.showinfo("Erro", "Erro ao cadastrar venda: %s"%(e))
    
            self.head.configure(text = "Confirmação")
            
            #Alteração tamanho da janela
            self.width=700
            self.height=500
            self.x = (self.screen_width // 2) - (self.width // 2)
            self.y = (self.screen_height // 2) - (self.height // 2)
            main_window.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
            
            self.frame_form = ctk.CTkFrame(main_window, fg_color='#EBEBEB')
            self.frame_form.pack(fill="both")
            self.inner_frame_form = ctk.CTkFrame(self.frame_form, fg_color='transparent')
            self.inner_frame_form.pack(pady = 25)
            
            #Criando campos com informações, preenchimento desabilitado
            self.name_label=ctk.CTkLabel(self.inner_frame_form, text="Nome", font=ctk.CTkFont("Segoe UI", 15, "bold"))
            self.name_label.grid(row=0, column=1, columnspan = 2)
            self.form_name = ctk.CTkEntry(self.inner_frame_form, height=40, width=435, corner_radius=15, border_color="#554131", justify = "center")
            self.form_name.grid(row=1, column=1, padx=15, sticky=N, columnspan = 2)
            self.form_name.insert(END, produto[1])
            
            self.form_name.configure(state = "disabled")
            
            self.price_label=ctk.CTkLabel(self.inner_frame_form, text="Valor Unidade", font=ctk.CTkFont("Segoe UI", 15, "bold"))
            self.price_label.grid(row=3, column=1, columnspan = 2)
            self.form_price = ctk.CTkEntry(self.inner_frame_form, height=40, width=435, corner_radius=15, border_color="#554131", justify = "center")
            self.form_price.grid(row=4, column=1, padx=15, sticky=E, columnspan = 2)
            self.form_price.insert(END, produto[3])
            self.form_price.configure(state = "disabled")
            
            self.valtotal_label=ctk.CTkLabel(self.inner_frame_form, text="Valor Total", font=ctk.CTkFont("Segoe UI", 15, "bold"))
            self.valtotal_label.grid(row=5, column=1, columnspan = 2)
            self.form_valtotal = ctk.CTkEntry(self.inner_frame_form, height=40, width=435, corner_radius=15, border_color="#554131", justify = "center")
            self.form_valtotal.grid(row=6, column=1, padx=14, sticky=W, columnspan = 2)
            quantidade = self.form_qtd.get()
            total = round(float(quantidade) * float(produto[3]), 2)
            self.form_valtotal.insert(END, total)
            self.form_valtotal.configure(state = "disabled")
            
            self.form_id.configure(state = "disabled", justify = "center")
            
            #Mudando posição do botão
            self.submit_button.pack_forget()
            self.submit_button.configure(text = "Confirmar", width = 435, command = self.cadastrarVenda(self.qtdProd))
            self.submit_button.pack(pady = 25)
            self.qtd_label.pack_forget()
            self.form_qtd.pack_forget()
            
            main_window.update()
        
        #Criando o formulário de criação de produto
        self.id_label=ctk.CTkLabel(main_window, text="Produto", font=ctk.CTkFont("Segoe UI", 15, "bold"))
        self.id_label.pack(anchor=S, pady = 8)
        self.form_id = ctk.CTkEntry(main_window, height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_id.pack(anchor=N)
        
        self.qtd_label=ctk.CTkLabel(main_window, text="Quantidade", font=ctk.CTkFont("Segoe UI", 15, "bold"))
        self.qtd_label.pack(anchor = S, pady = 8)
        self.form_qtd = ctk.CTkEntry(main_window, height=40, width=200, corner_radius=15, border_color="#554131")
        self.form_qtd.pack(anchor = N)
        
        #Botão cadastrar
        self.submit_button = ctk.CTkButton(main_window, text="Cadastrar", height=40, width=100, corner_radius=15, command=segundaTela, 
                                        fg_color="#554131", text_color="#EBEBEB", font=ctk.CTkFont(family="Segoe UI", weight="bold"))
        self.submit_button.pack(pady = 25)
        main_window.mainloop()
        
    #Função para cadastrar venda
    def cadastrarVenda(self, qtd2):
        id = self.form_id.get()
        qtd = self.form_qtd.get()
        nome = self.form_name.get()
        total = self.form_valtotal.get()
        if id == None or qtd == None or nome == None or total == None:
            main_window.destroy()
            messagebox.showinfo("Erro", "Não deixe nenhum campo vazio")
            GetProduto()
        else:
            try:
                self.dbVendas.insert(id, nome, qtd, total)
                main_window.destroy()
                messagebox.showinfo("Sucesso!", "Venda cadastrada com sucesso!")
                if self.callback:
                    self.callback()
                self.qtdProd = int(qtd2)-int(qtd)
                self.db.reduceQtd(id,self.qtdProd)
                GetProduto()
            except Exception as e:
                    main_window.destroy()
                    messagebox.showinfo("Erro", "Erro ao cadastrar venda: %s"%(e))
                                      
            
 