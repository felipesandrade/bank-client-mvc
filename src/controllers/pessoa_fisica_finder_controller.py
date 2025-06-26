from typing import Dict
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable
from src.models.sqlite.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface

class PessoaFisicaFinderController:
    def __init__(self, pessoa_fisica_repository: PessoaFisicaRepositoryInterface) -> None:
        self.__pessoa_fisica_repository = pessoa_fisica_repository

    def find(self, pessoa_fisica_id: int) -> Dict:
        pessoa_fisica_data = self.__find_pessoa_fisica_in_db(pessoa_fisica_id)
        formated_response = self.__format_response(pessoa_fisica_data)

        return formated_response

    def __find_pessoa_fisica_in_db(self, pessoa_fisica_id: int) -> PessoaFisicaTable:
        pessoa_fisica_data = self.__pessoa_fisica_repository.list_pessoa_fisica(pessoa_fisica_id)

        if not pessoa_fisica_id:
            raise Exception("Pessoa física não encontrada!")

        return pessoa_fisica_data

    def __format_response(self, pessoa_fisica_data: PessoaFisicaTable) -> Dict:
        return {
            "data": {
                "type": "Pessoa Física",
                "count": 1,
                "attributes": {
                    "nome_completo": pessoa_fisica_data.nome_completo,
                    "idade": pessoa_fisica_data.idade,
                    "celular": pessoa_fisica_data.celular,
                    "email": pessoa_fisica_data.email,
                    "categoria": pessoa_fisica_data.categoria,
                    "renda_mensal": pessoa_fisica_data.renda_mensal,
                    "saldo": pessoa_fisica_data.saldo
                }
            }
        }
    