# pylint: disable=unused-argument
from .pessoa_fisica_finder_controller import PessoaFisicaFinderController

class MockPessoaFisica:
    def __init__(self,
                renda_mensal,
                idade,
                nome_completo,
                celular,
                email,
                categoria,
                saldo) -> None:

        self.renda_mensal = renda_mensal
        self.idade = idade
        self.nome_completo = nome_completo
        self.celular = celular
        self.email = email
        self.categoria = categoria
        self.saldo = saldo

class MockPessoaFisicaRepository:
    def list_pessoa_fisica(self, pessoa_fisica_id: int):
        return MockPessoaFisica(
            renda_mensal = 5000,
            idade = 30,
            nome_completo = "Felipe Andrade",
            celular = "8588084593",
            email = "felipe@gmail.com",
            categoria = "categoria a",
            saldo = 100
        )

def test_find():
    controller = PessoaFisicaFinderController(MockPessoaFisicaRepository())
    response = controller.find(123)

    expected_response = {
            "data": {
                "type": "Pessoa Física",
                "count": 1,
                "attributes": {
                    "nome_completo": "Felipe Andrade",
                    "idade": 30,
                    "celular": "8588084593",
                    "email": "felipe@gmail.com",
                    "categoria": "categoria a",
                    "renda_mensal": 5000,
                    "saldo": 100
                }
            }
        }

    assert response == expected_response
