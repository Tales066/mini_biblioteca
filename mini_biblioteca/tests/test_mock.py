from unittest.mock import Mock

from biblioteca.biblioteca import Biblioteca
from biblioteca.livro import Livro


def test_consultar_livro_com_mock():

    livro = Livro(
        "123",
        "Python para Iniciantes",
        "Talyta",
        3
    )

    repositorio_mock = Mock()

    repositorio_mock.buscar_por_isbn.return_value = livro

    biblioteca = Biblioteca()
    biblioteca.repositorio = repositorio_mock

    resultado = biblioteca.consultar_livro("123")
    assert resultado == livro

    repositorio_mock.buscar_por_isbn.assert_called_once_with("123")


def test_cadastrar_livro_com_mock():

    livro = Livro(
        "123",
        "Python para Iniciantes",
        "Talyta",
        3
    )

    repositorio_mock = Mock()

    repositorio_mock.salvar.return_value = livro

    biblioteca = Biblioteca()
    biblioteca.repositorio = repositorio_mock
    
    resultado = biblioteca.cadastrar_livro(livro)

    assert resultado == livro

    repositorio_mock.salvar.assert_called_once_with(livro)
