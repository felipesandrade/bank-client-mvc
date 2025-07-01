import pytest
from .pessoa_juridica_creator_controller import PessoaJuridicaCreatorController

class MockPessoaJuridicaRepository:
    def insert_pessoa_juridica(self,
                                faturamento: float,
                                idade: int,
                                nome_fantasia: str,
                                celular: str,
                                email_corporativo: str,
                                categoria: str,
                                saldo: float
                               ):
        pass

def test_create():
    pessoa_juridica_info = {
        "faturamento": 5000,
        "idade": 25,
        "nome_fantasia": "Empresa Teste",
        "celular": "8599999999",
        "email_corporativo": "empresa.teste@teste.com",
        "categoria": "Categoria Teste",
        "saldo": 50
    }

    controller = PessoaJuridicaCreatorController(MockPessoaJuridicaRepository())
    response = controller.create(pessoa_juridica_info)

    assert response["data"]["type"] == "Pessoa Jurídica"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == pessoa_juridica_info

def test_create_error():
    pessoa_juridica_info = {
        "faturamento": 5000,
        "idade": 25,
        "nome_fantasia": "Empresa Teste123",
        "celular": "8599999999",
        "email_corporativo": "empresa.teste@teste.com",
        "categoria": "Categoria Teste",
        "saldo": 50
    }

    controller = PessoaJuridicaCreatorController(MockPessoaJuridicaRepository())

    with pytest.raises(Exception):
        controller.create(pessoa_juridica_info)
