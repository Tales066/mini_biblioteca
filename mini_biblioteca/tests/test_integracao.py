from biblioteca.biblioteca import Biblioteca
from biblioteca.livro import Livro


def test_fluxo_cadastro_consulta_disponibilidade_emprestimo():

    # Arrange
    biblioteca = Biblioteca()

    livro = Livro(
        "123",
        "Python para Iniciantes",
        "Talyta",
        3
    )

    biblioteca.cadastrar_livro(livro)

    livro_consultado = biblioteca.consultar_livro("123")

    disponivel_antes = biblioteca.verificar_disponibilidade("123")

    biblioteca.emprestar_livro("123")

    livro_depois = biblioteca.consultar_livro("123")

    assert livro_consultado == livro
    assert disponivel_antes is True
    assert livro_depois == livro
    assert livro_depois.quantidade == 2

    
def test_fluxo_completo_emprestimo_e_devolucao():

    biblioteca = Biblioteca()

    livro = Livro(
        "456",
        "Testes de Software",
        "Talyta",
        2
    )

    biblioteca.cadastrar_livro(livro)
    livro_consultado = biblioteca.consultar_livro("456")
    assert livro_consultado == livro
    assert livro_consultado.quantidade == 2
    biblioteca.emprestar_livro("456")
    livro_apos_emprestimo = biblioteca.consultar_livro("456")
    assert livro_apos_emprestimo.quantidade == 1
    assert biblioteca.verificar_disponibilidade("456") is True
    biblioteca.devolver_livro("456")

    livro_apos_devolucao = biblioteca.consultar_livro("456")

    assert livro_apos_devolucao.quantidade == 2
    assert biblioteca.verificar_disponibilidade("456") is True

