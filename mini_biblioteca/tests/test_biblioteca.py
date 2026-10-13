from biblioteca.livro import Livro


def test_cadastrar_livro(biblioteca, livro):

    resultado = biblioteca.cadastrar_livro(livro)

    assert resultado == livro


def test_consultar_livro(biblioteca, livro):

    biblioteca.cadastrar_livro(livro)

    resultado = biblioteca.consultar_livro("123")

    assert resultado == livro


def test_verificar_disponibilidade(biblioteca, livro):

    biblioteca.cadastrar_livro(livro)

    resultado = biblioteca.verificar_disponibilidade("123")

    assert resultado is True


def test_emprestar_livro(biblioteca, livro):

    biblioteca.cadastrar_livro(livro)

    biblioteca.emprestar_livro("123")

    assert livro.quantidade == 2


def test_devolver_livro(biblioteca, livro):

    biblioteca.cadastrar_livro(livro)

    biblioteca.devolver_livro("123")

    assert livro.quantidade == 4

