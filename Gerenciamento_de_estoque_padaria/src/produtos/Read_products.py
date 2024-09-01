from tkinter import *
from tkinter import ttk

class Read:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title("Produtos")
        self.main_window.geometry("1280x720+0+0")
        self.main_window.config(bg="#EBEBEB")
        self.main_window.state("zoomed")   
        
        self.frame1 = Frame(self.main_window, bg="#756645")
        self.frame1.pack(side=TOP, fill=Y, expand = False, ipadx = 1280)
        
        self.head = Label(self.frame1, text="Produtos", font=("MONTSERRAT", 22, "bold"), bg="#756645", fg="#F4EE82")
        self.head.pack(padx=10, pady=15) 
        
        self.table_frame=Frame(self.main_window, bg="white")
        self.table_frame.pack(anchor=CENTER, pady=25)
        self.table_style=ttk.Style()
        self.table=ttk.Treeview(self.table_frame, columns=(1, 2, 3, 4, 5))
        
        self.table.heading("1", text="ID")
        self.table.column("1", width=60, stretch=NO, anchor=CENTER)
        self.table.heading("2", text="PRODUTO")
        self.table.column("2", minwidth=120, stretch=NO, anchor=CENTER)
        self.table.heading("3", text="QUANT")
        self.table.column("3", minwidth=40, stretch=NO, anchor=CENTER)
        self.table.heading("4", text="VALOR")
        self.table.column("4", minwidth=60, stretch=NO, anchor=CENTER)
        self.table.heading("5", text="VALIDADE")
        self.table.column("5", minwidth=90, stretch=NO, anchor=CENTER)
        self.table["show"] = "headings"
        self.table.pack(fill=BOTH)
        self.table.insert(parent='', index=0, values=(1, "PÃO", 15, 20, "10-4-2025"))
        
        self.main_window.mainloop()
        
app=Read()

        
