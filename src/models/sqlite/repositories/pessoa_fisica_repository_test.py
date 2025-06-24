from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from .pessoa_fisica_repository import PessoaFisicaRepository

# Simulando uma conexão com o banco de dados
class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data = [
                (
                    [mock.call.query(PessoaFisicaTable)],
                    [PessoaFisicaTable(
                        id = 1,
                        renda_mensal = 1000.00,
                        idade = 40,
                        nome_completo = "Felipe Andrade",
                        celular = "85988084593",
                        email = "felipes.andrade@gmail.com",
                        categoria="A",
                        saldo = 5000.00
                    ),
                    PessoaFisicaTable(
                        id = 2,
                        renda_mensal = 10000.00,
                        idade = 38,
                        nome_completo = "Priscila Andrade",
                        celular = "85987878585",
                        email = "rosapriscilaom@gmail.com",
                        categoria="A",
                        saldo = 1000.00
                    )
                    ]
                )
            ]
        )

    def __enter__(self): return self

    def __exit__(self, exc_type, exc_val, exc_tb): pass

# Simulando uma conexão com o banco de dados para testar as exceções
class MockConnectionNoResult:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        # Quando a query for executada o efeito secundário é levantar o erro
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")

    def __enter__(self): return self

    def __exit__(self, exc_type, exc_val, exc_tb): pass

# Teste unitário
def test_list_pessoas_fisicas():
    mock_connection = MockConnection()
    repo = PessoaFisicaRepository(mock_connection)
    response = repo.list_pessoas_fisicas()

    # Veririca se a query foi chamada 1 vez com a tabela PessoaFisciaTable
    mock_connection.session.query.assert_called_once_with(PessoaFisicaTable)
    # Verifica se a propriedade all foi chamada 1 vez
    mock_connection.session.all.assert_called_once()
    #Verifica se a propriedade filter não foi chamda
    mock_connection.session.filter.assert_not_called()

    assert response[0].nome_completo == "Felipe Andrade"

def test_delete_pessoa_fisica():
    mock_connection = MockConnection()
    repo = PessoaFisicaRepository(mock_connection)
    repo.delete_pessoa_fisica(1)

    # Veririca se a query foi chamada 1 vez com a tabela PessoaFisciaTable
    mock_connection.session.query.assert_called_once_with(PessoaFisicaTable)
    # Verifica se a propriedade filter foi chamada passando o parametro id
    mock_connection.session.filter.assert_called_once_with(PessoaFisicaTable.id == 1)
    # Verifica se a propriedade delete foi chamda 1 vez
    mock_connection.session.delete.assert_called_once_with()

def test_list_pessoas_fisicas_no_result():
    mock_connection = MockConnectionNoResult()
    repo = PessoaFisicaRepository(mock_connection)
    response = repo.list_pessoas_fisicas()

    # Veririca se a query foi chamada 1 vez com a tabela PessoaFisciaTable
    mock_connection.session.query.assert_called_once_with(PessoaFisicaTable)
    # Verifica se a propriedade all foi chamada 1 vez
    mock_connection.session.all.assert_not_called()
    #Verifica se a propriedade filter não foi chamda
    mock_connection.session.filter.assert_not_called()

    assert response == []

def test_delete_pessoa_fisica_error():
    mock_connection = MockConnectionNoResult()
    repo = PessoaFisicaRepository(mock_connection)

    # Verifica se um erro foi lançado
    with pytest.raises(Exception):
        repo.delete_pessoa_fisica(1)

    mock_connection.session.rollback.assert_called_once()
    