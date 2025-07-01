
# pylint: disable=unused-argument
from .pessoa_juridica_finder_controller import PessaoJuridicaFinderController

class MockPessoaJuridica:
    def __init__(self,
                faturamento: float,
                idade: int,
                nome_fantasia: str,
                celular: str,
                email_corporativo: str,
                categoria: str,
                saldo: float) -> None:

        self.faturamento = faturamento
        self.idade = idade
        self.nome_fantasia = nome_fantasia
        self.celular = celular
        self.email_corporativo = email_corporativo
        self.categoria = categoria
        self.saldo = saldo

class MockPessoaJuridicaRepository:
    def list_pessoa_juridica(self, pessoa_fisica_id: int):
        return MockPessoaJuridica(
            faturamento = 80000,
            idade = 20,
            nome_fantasia =  "Empresa teste",
            celular = "859888084593",
            email_corporativo = "empresa.teste@yhaoo.com",
            categoria = "Categoria empresa",
            saldo = 90000
        )


def test_find():
    controller = PessaoJuridicaFinderController(MockPessoaJuridicaRepository())
    response = controller.find(123)

    expected_response = {
        "data": {
            "type": "Pessoa Jurídica",
            "count": 1,
            "attributes": {
                "faturamento": 80000,
                "idade": 20,
                "nome_fantasia":  "Empresa teste",
                "celular": "859888084593",
                'email_corporativo': "empresa.teste@yhaoo.com",
                "categoria": "Categoria empresa",
                "saldo": 90000
            }
        }
    }

    assert response == expected_response
