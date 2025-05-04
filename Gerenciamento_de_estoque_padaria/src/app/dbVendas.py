import sqlite3
from datetime import date
import os

class Data2:
    def __init__(self, dbVendas):
        # Conectando ao banco de dados
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        DB_PATH = os.path.join(BASE_DIR, '..', 'app', 'dist', 'data', dbVendas)
        self.con = sqlite3.connect(DB_PATH)
        self.cur = self.con.cursor()
        from src import Vendas

        # Criando a tabela se ela não existir
        vendas = """CREATE TABLE IF NOT EXISTS VendasPadaria(
                         ID INTEGER PRIMARY KEY,
                         IDProduto INTEGER,
                         Produto TEXT NOT NULL,
                         Data DATE NOT NULL,
                         Quantidade INTEGER NOT NULL,
                         PrecoTotal REAL NOT NULL
                    );"""       
        self.cur.execute(vendas)
        self.con.commit()

    # Inserindo uma venda
    def insert(self, IDProduto, Produto, Quantidade, PrecoTotal):
        Data = date.today()
        self.cur.execute("SELECT MAX(ID) FROM VendasPadaria")
        
        #Incrementa ID
        ID = self.cur.fetchone()[0]
        if ID is None:
            ID = 1
        else: 
            ID = ID+1
            
        #Insere no banco de dados   
        self.cur.execute("INSERT INTO VendasPadaria (ID, IDProduto, Produto, Data, Quantidade, PrecoTotal) VALUES (?, ?, ?, ?, ?, ?)",
                         (ID, IDProduto, Produto, Data, Quantidade, PrecoTotal))
        self.con.commit()

    # Obtendo todas as vendas
    def fetch(self):
        self.cur.execute("SELECT * FROM VendasPadaria")
        rows = self.cur.fetchall()
        return rows
   
    # Removendo uma venda por ID
    def remove(self, ID):
        self.cur.execute("DELETE FROM VendasPadaria WHERE ID = ?", (ID,))
        self.con.commit()

    # Fechando a conexão com o banco de dados
    def __del__(self):
        self.con.close()