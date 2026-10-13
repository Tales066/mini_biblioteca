import pytest

from biblioteca.livro import Livro
from biblioteca.validador import validar_livro


@pytest.mark.parametrize(
    "quantidade",
    [-1, 0, 1, 2]
)
def test_quantidade(quantidade):

    livro = Livro(
        "123",
        "Python para Iniciantes",
        "Talyta",
        quantidade
    )

    if quantidade < 0:
        with pytest.raises(ValueError):
            validar_livro(livro)
    else:
        validar_livro(livro)
        assert livro.quantidade == quantidade


@pytest.mark.parametrize(
    "quantidade, disponivel",
    [
        (0, False),
        (1, True),
        (2, True)
    ]
)
def test_disponibilidade(quantidade, disponivel):

    livro = Livro(
        "123",
        "Python para Iniciantes",
        "Talyta",
        quantidade
    )

    assert livro.esta_disponivel() is disponivel


@pytest.mark.parametrize(
    "isbn",
    ["123", "ABC123", "ISBN-001"]
)
def test_isbn_valido(isbn):

    livro = Livro(
        isbn,
        "Python para Iniciantes",
        "Talyta",
        2
    )

    assert livro.isbn == isbn
