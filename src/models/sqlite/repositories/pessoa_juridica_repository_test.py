from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pessoa_juridca import PessoaJuridicaTable
from .pessoa_juridica_repository import PessoaJurdicaRepository

class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data = [
                (
                    [mock.call.query(PessoaJuridicaTable)],
                    [PessoaJuridicaTable(
                        id = 1,
                        faturamento = 8000,
                        idade = 25,
                        nome_fantasia = "Empresa A",
                        celular = "85988084593",
                        email_corporativo = "empresa_a@empresa.com.br",
                        categoria = "Categoria A",
                        saldo = 50000
                    ),
                    PessoaJuridicaTable(
                        id = 2,
                        faturamento = 50000,
                        idade = 55,
                        nome_fantasia = "Empresa B",
                        celular = "85988084593",
                        email_corporativo = "empresa_b@empresa.com.br",
                        categoria = "Categoria B",
                        saldo = 15000
                    ),
                    ]
                )
            ]
        )

    def __enter__(self): return self

    def __exit__(self, exc_type, exc_val, exc_tb): pass

class MockConnectionNoResult:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found
        self.session.add.side_effect = self.__raise_no_result_found


    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")

    def __enter__(self): return self

    def __exit__(self, exc_type, exc_val, exc_tb): pass

def test_insert_pessoa_juridica():
    faturamento = 500000
    idade = 55
    nome_fantasia = "Empresa Prilipes"
    celular = "(85) 98808-4593"
    email_corporativo = "empresa_prilipes@gmail.com"
    categoria = "Empesa ABCD"
    saldo = 1000000

    mock_connection = MockConnection()
    repo = PessoaJurdicaRepository(mock_connection)
    repo.insert_pessoa_jurifica(faturamento=faturamento,
                                idade=idade,
                                nome_fantasia=nome_fantasia,
                                celular=celular,
                                email_corporativo=email_corporativo,
                                categoria=categoria,
                                saldo=saldo)

    mock_connection.session.add.assert_called()
    called_pessoa_juridica = mock_connection.session.add.call_args[0][0]
    assert isinstance(called_pessoa_juridica, PessoaJuridicaTable)
    assert called_pessoa_juridica.nome_fantasia == "Empresa Prilipes"

def test_list_pessoa_juridica():
    mock_connection = MockConnection()
    repo = PessoaJurdicaRepository(mock_connection)
    response = repo.list_pessoa_juridica()

    mock_connection.session.query.assert_called_once_with(PessoaJuridicaTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response[0].nome_fantasia == "Empresa A"

def test_delete_pessoa_jurifica():
    mock_connection = MockConnection()
    repo = PessoaJurdicaRepository(mock_connection)
    repo.delete_pessoa_juridica(1)

    mock_connection.session.query.assert_called_once_with(PessoaJuridicaTable)
    mock_connection.session.filter.assert_called_once_with(PessoaJuridicaTable.id == 1)
    mock_connection.session.delete.assert_called_once_with()

def test_list_pessoa_juridica_no_result():
    mock_connection = MockConnectionNoResult()
    repo = PessoaJurdicaRepository(mock_connection)
    response = repo.list_pessoa_juridica()

    mock_connection.session.query.assert_called_once_with(PessoaJuridicaTable)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()

    assert response == []

def test_delete_pessoa_jurifica_error():
    mock_connection = MockConnectionNoResult()
    repo = PessoaJurdicaRepository(mock_connection)

    with pytest.raises(Exception):
        repo.delete_pessoa_juridica(1)

    mock_connection.session.rollback.assert_called_once()

def test_pessoa_juridica_erro():
    faturamento = 500000
    idade = 55
    nome_fantasia = "Empresa Prilipes"
    celular = "(85) 98808-4593"
    email_corporativo = "empresa_prilipes@gmail.com"
    categoria = "Empesa ABCD"
    saldo = 1000000

    mock_connection = MockConnectionNoResult()
    repo = PessoaJurdicaRepository(mock_connection)

    with pytest.raises(Exception, match="No result found"):
        repo.insert_pessoa_jurifica(faturamento=faturamento,
                                    idade=idade,
                                    nome_fantasia=nome_fantasia,
                                    celular=celular,
                                    email_corporativo=email_corporativo,
                                    categoria=categoria,
                                    saldo=saldo)

    mock_connection.session.add.assert_called()
    mock_connection.session.rollback.assert_called()
