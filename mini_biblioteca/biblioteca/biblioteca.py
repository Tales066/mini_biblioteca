from biblioteca.repositorio import LivroRepository


class Biblioteca:

    def __init__(self):
        self.repositorio = LivroRepository()

    def cadastrar_livro(self, livro):
        return self.repositorio.salvar(livro)

    def consultar_livro(self, isbn):
        return self.repositorio.buscar_por_isbn(isbn)

    def verificar_disponibilidade(self, isbn):
        livro = self.consultar_livro(isbn)
        return livro.esta_disponivel()

    def emprestar_livro(self, isbn):
        livro = self.consultar_livro(isbn)
        livro.emprestar()
        return livro

    def devolver_livro(self, isbn):
        livro = self.consultar_livro(isbn)
        livro.devolver()
        return livro

    def listar_livros(self):
        return self.repositorio.listar()