from typing import Dict
from src.models.sqlite.entities.pessoa_juridca import PessoaJuridicaTable
from src.models.sqlite.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface
from .interfaces.pessoa_juridica_finder_controller import PessaoJuridicaFinderControllerInterface

class PessaoJuridicaFinderController(PessaoJuridicaFinderControllerInterface):
    def __init__(self, pessoa_juridica_repository: PessoaJuridicaRepositoryInterface) -> None:
        self.__pessoa_juridica_repository = pessoa_juridica_repository

    def find(self, pessoa_juridica_id: int) -> Dict:
        pessoa_juridica_data = self.__find_pessoa_juridica_in_db(pessoa_juridica_id)
        formated_response = self.__format_response(pessoa_juridica_data)

        return formated_response

    def __find_pessoa_juridica_in_db(self, pessoa_juridica_id: int) -> PessoaJuridicaTable:
        pessoa_juridica_data = self.__pessoa_juridica_repository.list_pessoa_juridica(pessoa_juridica_id)

        if not pessoa_juridica_id:
            raise Exception("Pessoa jurídica não encontrada!")

        return pessoa_juridica_data
  
    def __format_response(self, pessoa_juridica_data: PessoaJuridicaTable) -> Dict:
        return {
            "data": {
                "type": "Pessoa Jurídica",
                "count": 1,
                "attributes": {
                    "faturamento": pessoa_juridica_data.faturamento,
                    "idade": pessoa_juridica_data.idade,
                    "nome_fantasia": pessoa_juridica_data.nome_fantasia,
                    "celular": pessoa_juridica_data.celular,
                    "email_corporativo": pessoa_juridica_data.email_corporativo,
                    "categoria": pessoa_juridica_data.categoria,
                    "saldo": pessoa_juridica_data.saldo
                }
            }
        }
