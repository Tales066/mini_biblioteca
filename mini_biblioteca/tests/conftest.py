import pytest
from biblioteca.livro import Livro
from biblioteca.biblioteca import Biblioteca
from biblioteca.database import Database


@pytest.fixture
def livro():
    return Livro(
        "123",
        "Python para Iniciantes",
        "Talyta",
        3
    )


@pytest.fixture
def biblioteca():
    return Biblioteca()


@pytest.fixture
def banco_integracao(tmp_path):
    caminho = tmp_path / "biblioteca.db"

    banco = Database(str(caminho))
    banco.criar_tabela()

    yield banco

    banco.fechar()