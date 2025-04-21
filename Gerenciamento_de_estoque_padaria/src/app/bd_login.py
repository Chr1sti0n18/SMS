import sqlite3
import os

class Data:
    
    def __init__(self, bd_login):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(base_dir, '..', 'app', 'dist', 'data', bd_login)
        self.connect = sqlite3.connect(data_dir)
        self.cursor = self.connect.cursor()
        usuarios = """CREATE TABLE IF NOT EXISTS UsuariosPadaria(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        NomeUser TEXT NOT NULL,
                        Senha TEXT NOT NULL,
                        NivelAcess TEXT DEFAULT 'Funcionario'
                        );"""
        self.cursor.execute(usuarios)
        self.connect.commit()

    def insert(self, nome, senha, nivel_acesso):
        self.cursor.execute("INSERT INTO UsuariosPadaria (NomeUser, Senha, NivelAcess) VALUES (?, ?, ?)", (nome, senha, nivel_acesso))
        self.connect.commit()

    def fetch(self):
        self.cursor.execute("SELECT * FROM UsuariosPadaria")
        rows = self.cursor.fetchall()
        return rows

    def remove(self, id):
        self.cursor.execute("DELETE FROM UsuariosPadaria WHERE ID =?", (id,))
        self.connect.commit()

    def update(self, nome, senha, nivel_acesso, ID):
        self.cursor.execute("""UPDATE UsuariosPadaria SET NomeUser=?, Senha=?, NivelAcess=?
                            WHERE ID=?""", (nome, senha, nivel_acesso, ID))
        self.connect.commit()

    def logar(self, nome, senha):
        self.cursor.execute("SELECT * FROM UsuariosPadaria WHERE NomeUser='%s' AND Senha='%s'"%(nome, senha))
        rows = self.cursor.fetchone()
        return rows
    

    def trocarSenha(self, id, novaSenha):
        try:
            self.cursor.execute("UPDATE funcionarios SET senha=? WHERE id=?",
                         (novaSenha, id))
            self.connect.commit()
            return True

        except:
            return False
    