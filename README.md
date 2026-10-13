# Mini Biblioteca 

Projeto da disciplina teste de software, desenvolvido em Python para gerenciamento de livros, permitindo cadastrar, consultar, verificar disponibilidade, realizar empréstimos e devoluções, além de armazenar dados utilizando SQLite.

O projeto também conta com testes automatizados para verificar o funcionamento das funcionalidades e a qualidade do código.

## Tecnologias utilizadas

- **Python 3.11:** linguagem utilizada no desenvolvimento.
- **SQLite:** banco de dados para persistência das informações.
- **pytest:** framework para execução de testes automatizados.
- **pytest-cov:** ferramenta para medir a cobertura dos testes.
- **unittest:** biblioteca para criação de testes unitários.
- **unittest.mock:** ferramenta para simular dependências durante os testes.

## Estrutura do projeto

```text
mini_biblioteca/
│
├── biblioteca/
│   ├── _init_.py
│   ├── livro.py
│   ├── biblioteca.py
│   ├── repositorio.py
│   ├── validador.py
│   ├── database.py
│   ├── excecoes.py
│   └── _init_.py
│
├── tests/
│   ├── conftest.py
│   ├── test_livro.py
│   ├── test_biblioteca.py
│   ├── test_unittest.py
│   ├── test_parametrizacao.py
│   ├── test_excecoes.py
│   ├── test_mock.py
│   ├── test_side_effect.py
│   ├── test_integracao.py
│   ├── test_persistencia.py
│   ├── test_integracao_fixture.py
│   └── test_cobertura.py
│
├── requerimentos.txt
└──.venv/
```

### Descrição das pastas e arquivos

**Pasta `biblioteca/`**

Contém o código principal da aplicação.

- `livro.py`: define a classe Livro e as operações de empréstimo e devolução.
- `biblioteca.py`: implementa as operações principais da biblioteca.
- `repositorio.py`: realiza o cadastro, a consulta e a listagem dos livros.
- `validador.py`: verifica se os dados dos livros são válidos.
- `database.py`: implementa a persistência dos dados utilizando SQLite.
- `excecoes.py`: módulo destinado às exceções personalizadas, caso utilizadas.
- `_init_.py`: arquivo presente na estrutura do projeto.

**Pasta `tests/`**

Contém os testes automatizados.

- `conftest.py`: define fixtures compartilhadas.
- `test_livro.py`: testa a classe Livro.
- `test_biblioteca.py`: testa as funcionalidades da biblioteca.
- `test_unittest.py`: contém testes utilizando unittest.
- `test_parametrizacao.py`: testa diferentes valores utilizando parametrização.
- `test_excecoes.py`: verifica o tratamento de exceções.
- `test_mock.py`: utiliza mocks para simular dependências.
- `test_side_effect.py`: simula diferentes comportamentos e erros.
- `test_integracao.py`: verifica o funcionamento integrado das funcionalidades.
- `test_persistencia.py`: testa a persistência dos dados no SQLite.
- `test_integracao_fixture.py`: utiliza fixtures nos testes de integração.
- `test_cobertura.py`: contém testes adicionais para aumentar a cobertura do código.

## Instalação e configuração

### 1. Pré-requisitos

É necessário ter Python 3.11 instalado e a integração SQLite funcionando no Python.

Verifique a versão do Python:

```bash
python3.11 --version
```

Verifique o SQLite:

```bash
python3.11 -c "import sqlite3; print(sqlite3.sqlite_version)"
```

### 2. Acessar a pasta do projeto

```bash
cd ~/Downloads/mini_biblioteca
```

### 3. Criar o ambiente virtual

Execute este comando somente se o ambiente virtual ainda não existir:

```bash
python3.11 -m venv .venv
```

### 4. Ativar o ambiente virtual

```bash
source .venv/bin/activate
```

Após a ativação, o terminal deverá apresentar `(.venv)`.

### 5. Verificar o pip

```bash
python -m pip --version
```

Se o pip estiver instalado, atualize-o:

```bash
python -m pip install --upgrade pip
```

Se o pip não estiver disponível, tente:

```bash
python -m ensurepip --upgrade
```

### 6. Instalar as dependências

Instale o pytest e a ferramenta de cobertura:

```bash
python -m pip install pytest pytest-cov
```

Opcionalmente, crie um arquivo chamado `requerimentos.txt` com o seguinte conteúdo:

```text
pytest
pytest-cov
```

Depois, instale as dependências pelo arquivo:

```bash
python -m pip install -r requerimentos.txt
```

## Execução dos testes

Os comandos devem ser executados na pasta principal do projeto, com o ambiente virtual ativado.

### Executar todos os testes

```bash
python -m pytest
```

### Executar todos os testes com detalhes

```bash
python -m pytest -v
```

### Executar os testes com unittest

```bash
python -m unittest discover -s tests -v
```

### Executar testes específicos

Testes dos livros:

```bash
python -m pytest tests/test_livro.py -v
```

Testes da biblioteca:

```bash
python -m pytest tests/test_biblioteca.py -v
```

Testes parametrizados:

```bash
python -m pytest tests/test_parametrizacao.py -v
```

Testes de exceções:

```bash
python -m pytest tests/test_excecoes.py -v
```

Testes com Mock:

```bash
python -m pytest tests/test_mock.py -v
```

Testes com side_effect:

```bash
python -m pytest tests/test_side_effect.py -v
```

Testes de integração:

```bash
python -m pytest tests/test_integracao.py -v
```

Testes de persistência SQLite:

```bash
python -m pytest tests/test_persistencia.py -v
```

Testes de integração com fixtures:

```bash
python -m pytest tests/test_integracao_fixture.py -v
```

Testes adicionais de cobertura:

```bash
python -m pytest tests/test_cobertura.py -v
```

## Cobertura de testes

A cobertura permite verificar quais partes do código foram executadas durante os testes.

### Exibir o percentual de cobertura

```bash
python -m pytest --cov=biblioteca
```

### Exibir as linhas não cobertas

```bash
python -m pytest --cov=biblioteca --cov-report=term-missing
```

Desativar o ambiente virtual:

```bash
deactivate
```

Para executar os testes com relatório de cobertura:

```bash
python -m pytest --cov=biblioteca --cov-report=term-missing
```
