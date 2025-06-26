import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pessoa_fisica_repository import PessoaFisicaRepository
from .pessoa_juridica_repository import PessoaJurdicaRepository

db_connection_handler.connect_to_db()

# Skipando o teste de integração com o decorador do Pytest
@pytest.mark.skip(reason="Integração com o banco de dados")
def test_list_pessoas_fisicas():
    repo = PessoaFisicaRepository(db_connection_handler)
    response = repo.list_pessoas_fisicas()
    print()
    print(response)

# Skipando o teste de integração com o decorador do Pytest
@pytest.mark.skip(reason="Integração com o banco de dados")
def test_delete_pessoa_fisica():
    pessoa_fisica_id = 3

    repo = PessoaFisicaRepository(db_connection_handler)
    repo.delete_pessoa_fisica(pessoa_fisica_id)

# Skipando o teste de integração com o decorador do Pytest
@pytest.mark.skip(reason="Integração com o banco de dados")
def test_list_pessoas_juridicas():
    repo = PessoaJurdicaRepository(db_connection_handler)
    response = repo.list_pessoas_juridicas()
    print()
    print(response)

# Skipando o teste de integração com o decorador do Pytest
@pytest.mark.skip(reason="Integração com o banco de dados")
def test_delete_pessoa_juridica():
    pessoa_juridica_id = 3

    repo = PessoaJurdicaRepository(db_connection_handler)
    repo.delete_pessoa_juridica(pessoa_juridica_id)

# Skipando o teste de integração com o decorador do Pytest
@pytest.mark.skip(reason="Integração com o banco de dados")
def test_insert_pessoa_juridica():
    repo = PessoaJurdicaRepository(db_connection_handler)
    repo.insert_pessoa_jurifica(faturamento = 10000,
                                idade = 45,
                                nome_fantasia = "Empresa C",
                                celular = "8587878585",
                                email_corporativo = "empresa_c@empresa.com.br",
                                categoria = "Categoria A",
                                saldo = 1000000)

# Skipando o teste de integração com o decorador do Pytest
@pytest.mark.skip(reason="Integração com o banco de dados")
def test_insert_pessoa_fisica():
    repo = PessoaFisicaRepository(db_connection_handler)
    repo.insert_pessoa_fisica(renda_mensal = 10000,
                            idade = 55,
                            nome_completo = "Isabela Andrade",
                            celular = "8598787-8585",
                            email = "isabela@gmail.com",
                            categoria = "Categoria D",
                            saldo = 500 )
