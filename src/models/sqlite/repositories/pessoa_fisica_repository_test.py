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
        self.session.add.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")

    def __enter__(self): return self

    def __exit__(self, exc_type, exc_val, exc_tb): pass

def test_insert_pessoa_fisica():
    renda_mensal = 15000
    idade = 65
    nome_completo = "Raphael"
    celular = "85999999999"
    email = "raphael@gmail.com"
    categoria = "Pessoa Física ABC"
    saldo = 100

    mock_connection = MockConnection()
    repo = PessoaFisicaRepository(mock_connection)
    repo.insert_pessoa_fisica(renda_mensal=renda_mensal,
                              idade=idade,
                              nome_completo=nome_completo,
                              celular=celular,
                              email=email,
                              categoria=categoria,
                              saldo=saldo)

    mock_connection.session.add.assert_called()
    called_pessoa_fisica = mock_connection.session.add.call_args[0][0]
    assert isinstance(called_pessoa_fisica, PessoaFisicaTable)
    assert called_pessoa_fisica.nome_completo == "Raphael"

# Teste unitário
def test_list_pessoas_fisicas():
    mock_connection = MockConnection()
    repo = PessoaFisicaRepository(mock_connection)
    response = repo.list_pessoa_fisica()

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
    response = repo.list_pessoa_fisica()

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

def test_insert_pessoa_fisica_error():
    renda_mensal = 15000
    idade = 65
    nome_completo = "Raphael"
    celular = "85999999999"
    email = "raphael@gmail.com"
    categoria = "Pessoa Física ABC"
    saldo = 100

    mock_connection = MockConnectionNoResult()
    repo = PessoaFisicaRepository(mock_connection)

    with pytest.raises(Exception, match="No result found"):
        repo.insert_pessoa_fisica(
                                renda_mensal=renda_mensal,
                                idade=idade,
                                nome_completo=nome_completo,
                                celular=celular,
                                email=email,
                                categoria=categoria,
                                saldo=saldo
                                )

    mock_connection.session.add.assert_called()
    mock_connection.session.rollback.assert_called()
