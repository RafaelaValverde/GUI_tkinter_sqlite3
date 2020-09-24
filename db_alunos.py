import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS alunos (id INTEGER PRIMARY KEY, nome text, endereco text, curso text, rg text, ra text)")
        self.conn.commit()

    def insert(self, nome, endereco, curso, rg, ra):
        self.cur.execute("INSERT INTO alunos VALUES (NULL, ?, ?, ?, ?, ?)",
                         (nome, endereco, curso, rg, ra))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
