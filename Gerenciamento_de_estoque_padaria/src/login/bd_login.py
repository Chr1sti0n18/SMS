import sqlite3

class Database :
    
    def __init__(self, bd_login):
        self.connect = sqlite3.connect(bd_login)
        self.cursor = self.connect.cursor()
        usuarios = """CREATE TABLE IF NOT EXISTS UsuariosPadaria(
                        ID INTEGER AUTO_INCREMENT PRIMARY KEY,
                        NomeUser TEXT NOT NULL,
                        Senha TEXT NOT NULL,
                        NivelAcess TEXT DEFAULT 'Funcionario'
                        );"""
        self.cursor.execute(usuarios)
        self.connect.commit()

    def insert(self, nome, senha, nivel_acesso):
        self.cursor.execute("INSERT INTO UsuariosPadaria VALUES (NULL, ?, ?, ?)", (nome, senha, nivel_acesso))
        self.connect.commit()

    def fetch(self):
        self.cursor.execute("SELECT * FROM UsuariosPadaria")
        rows = self.cursor.fetchall()
        return rows

    def remove(self, id):
        self.cursor.execute("DELETE FROM UsuariosPadaria WHERE ID = ?", id)
        self.connect.commit()

    def update(self, id, nome, senha, nivel_acesso):
        self.cursor.execute("UPDATE UsuariosPadaria SET NomeUser=?, Senha=?, NivelAcess=?", (id, nome, senha, nivel_acesso))
        self.connect.commit()

    def logar(self, nome, senha):
        self.cursor.execute("SELECT * FROM UsuariosPadaria WHERE NomeUser='%s' AND Senha='%s'"%(nome, senha))
        rows = self.cursor.fetchone()
        return rows
    

#     def trocarSenha(self, id, novaSenha):
#         try:
#             self.cur.execute("UPDATE funcionarios SET senha=? WHERE id=?",
#                          (novaSenha, id))
#             self.con.commit()
#             return True

#         except:
#             return False
    