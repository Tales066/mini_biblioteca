def validar_livro(livro):

    if not livro.isbn:
        raise ValueError("ISBN é obrigatório.")

    if not livro.titulo:
        raise ValueError("Título é obrigatório.")

    if not livro.autor:
        raise ValueError("Autor é obrigatório.")

    if not isinstance(livro.quantidade, int):
        raise ValueError("Quantidade deve ser um número inteiro.")

    if livro.quantidade < 0:
        raise ValueError("Quantidade não pode ser negativa.")