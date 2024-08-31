from tkinter import *
from tkinter import ttk

class Read:
    def __init__(self):
        self.main_windown = Tk()
        self.main_windown.title("Produtos")
        self.main_windown.geometry("1600x900+0+0")
        self.main_windown.config(bg="#2c3e50")
        self.main_windown.state("zoomed")

        self.frame1 = Frame(self.main_windown, bg="#535c68")
        self.frame1.pack(side=TOP, fill=X)
        self.title= Label(self.frame1, text="Visualizar produtos", font=("CENTURY GOTHIC", 18, "bold"), bg="#535c68",
                            fg="white")
                                            #espaçamento 
        self.titulo.grid(row=0, columnspan=2, padx=10, pady=10, sticky="w")
        self.frame2 = Frame(self.frame1, bg="#535c68")
        self.frame2.grid(row=6, column=0, columnspan=4, padx=10, pady=10, sticky="w")

        self.btnDel = Button(self.frame2, text="Deletar", width=15, font=("CENTURY GOTHIC", 16, "bold"), fg="white",
                             bg="#16a085", command=self.del_cliente)
        self.btnDel.grid(row=0, column=0)

        self.frame3 = Frame(self.main_windown, bg="#ecf0f1")
        self.frame3.place(x=0, y=150, width=1980, height=520)

        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview", font=("CENTURY GOTHIC, 18"), rowheight=50)
        self.style.configure("mystyle.Treeview", font=("CENTURY GOTHIC, 18"))
        self.tv = ttk.Treeview(self.frame3, columns=(1, 2, 3, 4, 5), style="mystyle.Treeview")
        self.tv.heading("1", text="ID")
        self.tv.column("1", width=40, stretch=NO)
        self.tv.heading("2", text="Categoria")
        self.tv.column("5", width=200, stretch=NO)
        self.tv.heading("2", text="Nome")
        self.tv.column("5", width=200, stretch=NO)
        self.tv.heading("6", text="Preço")
        self.tv.column("6", width=150, stretch=NO)
        self.tv.heading("7", text="Quantidade")
        self.tv.column("7", width=300, stretch=NO)
        self.tv["show"] = "headings"

        self.tv.bind("<ButtonRelease-1>", self.getData)
        self.tv.pack(fill=X)
        self.displayAll()
        mainloop()