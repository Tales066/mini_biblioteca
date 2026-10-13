from biblioteca.livro import Livro


def test_criar_livro(livro):
    resultado = livro

    resultado = livro
    assert isinstance(resultado, Livro)


def test_isbn(livro):

    assert livro.isbn == "123"


def test_titulo(livro):

    assert livro.titulo == "Python para Iniciantes"


def test_autor(livro):

    assert livro.autor == "Talyta"


def test_quantidade(livro):

    assert livro.quantidade == 3


def test_disponibilidade(livro):

    assert livro.esta_disponivel() is True


def test_emprestimo(livro):

    livro.emprestar()

    assert livro.quantidade == 2


def test_devolucao(livro):

    livro.devolver()

    assert livro.quantidade == 4
