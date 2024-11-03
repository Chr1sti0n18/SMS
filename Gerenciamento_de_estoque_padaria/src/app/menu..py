import tkinter as tk
import customtkinter as ctk


class Menu:
    def __init__(self, id):
        self.main_window = tk.Tk()
        self.main_window.title("Menu")
        self.main_window.state("zoomed")
        screen_width = self.main_window.winfo_width()

        self.frame1 = ctk.CTkFrame(self.main_window)
        self.frame1.pack(side="top", fill="y", expand = False, ipadx = 1280)


        
        # Texto do inner frame
        self.head = ctk.CTkLabel(self.frame1, text="Menu", font=("Segoe Script", 52, "bold"), 
                                 fg_color="#FFC07E", text_color="#554131", height=120, width=screen_width, anchor="center")
        self.head.pack(fill="both")

        self.frame_buttons = ctk.CTkFrame(self.main_window, fg_color="transparent")
        self.frame_buttons.pack(anchor="n", pady=260)
        self.read_button = ctk.CTkButton(self.frame_buttons, text="Gerenciar Produtos", width=400, height= 300, font=ctk.CTkFont("Segoe Script"))
        self.read_button.grid(row=0, column=0, padx=50)
        self.read_button = ctk.CTkButton(self.frame_buttons, text="Gerenciar Usuários", width=400, height= 300)
        self.read_button.grid(row=0, column=1, padx=50)

        self.main_window.mainloop()

app = Menu(12311)