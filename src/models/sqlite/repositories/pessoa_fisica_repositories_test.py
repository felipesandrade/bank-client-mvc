from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from .pessoa_fisica_repositories import PessoaFisicaRepository

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
    