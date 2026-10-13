from biblioteca.livro import Livro


def test_salvar_livro_com_fixture(banco_integracao):

    livro = Livro(
        "111",
        "Python Avançado",
        "Talyta",
        4
    )

    banco_integracao.salvar_livro(livro)

    resultado = banco_integracao.buscar_por_isbn("111")

    assert resultado is not None
    assert resultado[0] == "111"
    assert resultado[1] == "Python Avançado"
    assert resultado[2] == "Talyta"
    assert resultado[3] == 4


def test_buscar_livro_com_fixture(banco_integracao):

    livro = Livro(
        "222",
        "Testes de Software",
        "Talyta",
        2
    )

    banco_integracao.salvar_livro(livro)

    resultado = banco_integracao.buscar_por_isbn("222")

    assert resultado is not None
    assert resultado[0] == "222"
    assert resultado[3] == 2
