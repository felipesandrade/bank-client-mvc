import pytest
from .pessoa_fisica_creator_controller import PessoaFisicaCreatorController

class MockPessoaFisicaRepository:
    def insert_pessoa_fisica(self,
                            renda_mensal: float,
                            idade: int,
                            nome_completo: str,
                            celular: str,
                            email: str,
                            categoria: str,
                            saldo: float):
        pass

def test_create():
    pessoa_fisica_info = {
        "renda_mensal": 15000,
        "idade": 30,
        "nome_completo": "Felipe Andrade",
        "celular": "8598808-4593",
        "email": "felipe@gmail.com",
        "categoria": "Categoria A",
        "saldo": 10000
    }
    controller = PessoaFisicaCreatorController(MockPessoaFisicaRepository())
    response = controller.create(pessoa_fisica_info)

    assert response["data"]["type"] == "Pessoa Física"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == pessoa_fisica_info

def test_create_error():
    pessoa_fisica_info = {
        "renda_mensal": 15000,
        "idade": 30,
        "nome_completo": "Felipe Andrade123",
        "celular": "8598808-4593",
        "email": "felipe@gmail.com",
        "categoria": "Categoria A",
        "saldo": 10000
    }
    controller = PessoaFisicaCreatorController(MockPessoaFisicaRepository())

    with pytest.raises(Exception):
        controller.create(pessoa_fisica_info)
