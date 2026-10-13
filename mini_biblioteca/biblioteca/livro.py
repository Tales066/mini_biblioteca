class Livro:

    def __init__(self, isbn, titulo, autor, quantidade):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.quantidade = quantidade

    def esta_disponivel(self):
        return self.quantidade > 0

    def emprestar(self):
        if self.quantidade <= 0:
            raise ValueError("Não há exemplares disponíveis.")

        self.quantidade -= 1

    def devolver(self):
        self.quantidade += 1