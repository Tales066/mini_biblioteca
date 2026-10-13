import pytest

from biblioteca.livro import Livro
from biblioteca.validador import validar_livro


def test_livro_sem_titulo():
    livro = Livro(
        "123",
        "",
        "Talyta",
        3
    )

    with pytest.raises(ValueError, match="Título é obrigatório."):
        validar_livro(livro)


def test_livro_sem_autor():
    livro = Livro(
        "456",
        "Python para Iniciantes",
        "",
        3
    )

    with pytest.raises(ValueError, match="Autor é obrigatório."):
        validar_livro(livro)


def test_quantidade_nao_inteira():
    livro = Livro(
        "789",
        "Python e Testes",
        "Talyta",
        "3"
    )

    with pytest.raises(
        ValueError,
        match="Quantidade deve ser um número inteiro."
    ):
        validar_livro(livro)