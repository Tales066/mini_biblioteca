from biblioteca.validador import validar_livro


class LivroRepository:

    def __init__(self):
        self.livros = {}

    def salvar(self, livro):

        validar_livro(livro)

        if livro.isbn in self.livros:
            raise ValueError("Livro já cadastrado.")

        self.livros[livro.isbn] = livro

        return livro

    def buscar_por_isbn(self, isbn):

        if isbn not in self.livros:
            raise ValueError("Livro não encontrado.")

        return self.livros[isbn]

    def listar(self):
        return list(self.livros.values())