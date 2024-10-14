import sqlite3

class Database:
    
    def __init__(self, bdProdutos):
        # Conectando ao banco de dados
        self.con = sqlite3.connect(bdProdutos)
        self.cur = self.con.cursor()
        
        # Criando a tabela se ela não existir
        produtos = """CREATE TABLE IF NOT EXISTS ProdutosPadaria(
                         ID INTEGER PRIMARY KEY AUTOINCREMENT,
                         Produto TEXT NOT NULL,
                         Quantidade INTEGER NOT NULL,
                         Preco REAL NOT NULL,
                         Validade DATE NOT NULL,
                         Categoria TEXT NOT NULL
                    );"""
        self.cur.execute(produtos)
        self.con.commit()

    # Inserindo um produto
    def insert(self, Produto, Quantidade, Preco, Validade, Categoria):
        self.cur.execute("INSERT INTO ProdutosPadaria (Produto, Quantidade, Preco, Validade, Categoria) VALUES (?, ?, ?, ?, ?)",
                         (Produto, Quantidade, Preco, Validade, Categoria))
        self.con.commit()

    # Obtendo todos os produtos
    def fetch(self, filter):
        if filter == "Todos":     
            self.cur.execute("SELECT * FROM ProdutosPadaria")
            rows = self.cur.fetchall()
            return rows
        self.cur.execute("SELECT * FROM ProdutosPadaria WHERE Categoria = ?", (filter,))
        rows = self.cur.fetchall()
        return rows
    
    # Obtendo um produto por nome
    def search(self, search):
        self.cur.execute("SELECT * FROM ProdutosPadaria WHERE Produto = ?", (search,))
        rows = self.cur.fetchall()
        return rows
    
    # Removendo um produto por ID
    def remove(self, ID):
        self.cur.execute("DELETE FROM ProdutosPadaria WHERE ID =?", (ID,))
        self.con.commit()

    # Atualizando um produto
    def update(self, ID, Produto, Quantidade, Preco, Validade, Categoria):
        self.cur.execute("""UPDATE ProdutosPadaria 
                            SET Produto = ?, Quantidade = ?, Preco = ?, Validade = ?, Categoria = ? 
                            WHERE ID = ?""",
                         (Produto, Quantidade, Preco, Validade, Categoria, ID))
        self.con.commit()

    # Fechando a conexão com o banco de dados
    def __del__(self):
        self.con.close()