import unittest

import pytest

from biblioteca.livro import Livro
from biblioteca.biblioteca import Biblioteca
from biblioteca.validador import validar_livro


def test_cadastro_livro_invalido():

    livro = Livro(
        "",
        "Python para Iniciantes",
        "Talyta",
        3
    )

    with pytest.raises(ValueError):
        validar_livro(livro)


def test_cadastro_livro_duplicado():

    biblioteca = Biblioteca()

    livro = Livro(
        "123",
        "Python para Iniciantes",
        "Talyta",
        3
    )

    biblioteca.cadastrar_livro(livro)

    with pytest.raises(ValueError):
        biblioteca.cadastrar_livro(livro)


def test_emprestar_livro_inexistente():

    biblioteca = Biblioteca()

    with pytest.raises(ValueError):
        biblioteca.emprestar_livro("999")


def test_emprestar_livro_sem_estoque():

    biblioteca = Biblioteca()

    livro = Livro(
        "123",
        "Python para Iniciantes",
        "Talyta",
        0
    )

    biblioteca.cadastrar_livro(livro)

    with pytest.raises(ValueError):
        biblioteca.emprestar_livro("123")


def test_devolver_livro_inexistente():

    biblioteca = Biblioteca()

    with pytest.raises(ValueError):
        biblioteca.devolver_livro("999")


class TestExcecoesComUnittest(unittest.TestCase):

    def test_livro_sem_estoque(self):

        livro = Livro(
            "123",
            "Python para Iniciantes",
            "Talyta",
            0
        )

        with self.assertRaises(ValueError):
            livro.emprestar()


if __name__ == "__main__":
    unittest.main()
