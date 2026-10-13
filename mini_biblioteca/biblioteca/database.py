import sqlite3


class Database:

    def __init__(self, caminho=":memory:"):
        self.conexao = sqlite3.connect(caminho)

    def criar_tabela(self):

        self.conexao.execute("""
            CREATE TABLE IF NOT EXISTS livros (
                isbn TEXT PRIMARY KEY,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                quantidade INTEGER NOT NULL
            )
        """)

        self.conexao.commit()

    def salvar_livro(self, livro):

        self.conexao.execute("""
            INSERT INTO livros (isbn, titulo, autor, quantidade)
            VALUES (?, ?, ?, ?)
        """, (
            livro.isbn,
            livro.titulo,
            livro.autor,
            livro.quantidade
        ))

        self.conexao.commit()

    def buscar_por_isbn(self, isbn):

        cursor = self.conexao.execute("""
            SELECT isbn, titulo, autor, quantidade
            FROM livros
            WHERE isbn = ?
        """, (isbn,))

        return cursor.fetchone()

    def fechar(self):
        self.conexao.close()
