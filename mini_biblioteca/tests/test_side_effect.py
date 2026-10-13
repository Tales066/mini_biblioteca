from unittest.mock import Mock

import pytest

from biblioteca.biblioteca import Biblioteca
from biblioteca.livro import Livro


def test_buscar_livro_com_side_effect_sucesso():

    livro = Livro(
        "123",
        "Python para Iniciantes",
        "Talyta",
        3
    )

    repositorio_mock = Mock()

    repositorio_mock.buscar_por_isbn.side_effect = lambda isbn: livro

    biblioteca = Biblioteca()
    biblioteca.repositorio = repositorio_mock

    resultado = biblioteca.consultar_livro("123")

    assert resultado == livro


def test_buscar_livro_com_side_effect_erro():

    repositorio_mock = Mock()

    repositorio_mock.buscar_por_isbn.side_effect = ValueError(
        "Livro não encontrado."
    )

    biblioteca = Biblioteca()
    biblioteca.repositorio = repositorio_mock

    with pytest.raises(ValueError, match="Livro não encontrado."):
        biblioteca.consultar_livro("999")
