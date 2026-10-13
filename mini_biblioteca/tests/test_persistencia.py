from biblioteca.livro import Livro
from biblioteca.database import Database


def test_persistencia_livro_sqlite():

    banco = Database()
    banco.criar_tabela()

    livro = Livro(
        "789",
        "Python e Testes",
        "Talyta",
        5
    )

    banco.salvar_livro(livro)
    resultado = banco.buscar_por_isbn("789")
    assert resultado is not None

    assert resultado[0] == "789"
    assert resultado[1] == "Python e Testes"
    assert resultado[2] == "Talyta"
    assert resultado[3] == 5

    banco.fechar()
