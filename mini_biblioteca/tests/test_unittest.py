import unittest

from biblioteca.livro import Livro
from biblioteca.biblioteca import Biblioteca


class TestLivro(unittest.TestCase):

    def test_criar_livro(self):

        livro = Livro(
            "123",
            "Python para Iniciantes",
            "Talyta",
            3
        )

        self.assertIsInstance(livro, Livro)

    def test_isbn(self):

        livro = Livro(
            "123",
            "Python para Iniciantes",
            "Talyta",
            3
        )

        self.assertEqual(livro.isbn, "123")

    def test_disponibilidade(self):

        livro = Livro(
            "123",
            "Python para Iniciantes",
            "Talyta",
            3
        )

        self.assertTrue(livro.esta_disponivel())

    def test_livro_indisponivel(self):

        livro = Livro(
            "123",
            "Python para Iniciantes",
            "Talyta",
            0
        )

        self.assertFalse(livro.esta_disponivel())


class TestBiblioteca(unittest.TestCase):

    def test_cadastrar_livro(self):

        biblioteca = Biblioteca()

        livro = Livro(
            "123",
            "Python para Iniciantes",
            "Talyta",
            3
        )

        resultado = biblioteca.cadastrar_livro(livro)

        self.assertEqual(resultado, livro)

    def test_emprestar_livro(self):

        biblioteca = Biblioteca()

        livro = Livro(
            "123",
            "Python para Iniciantes",
            "Talyta",
            3
        )

        biblioteca.cadastrar_livro(livro)

        biblioteca.emprestar_livro("123")

        self.assertEqual(livro.quantidade, 2)


if __name__ == "__main__":
    unittest.main()
