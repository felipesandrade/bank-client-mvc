import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pessoa_fisica_repositories import PessoaFisicaRepository

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
