import re
from typing import Dict
from src.models.sqlite.entities.pessoa_juridca import PessoaJuridicaTable
from src.models.sqlite.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface
from .interfaces.pessoa_juridica_creator_controller import PessoaJuridicaCreatorControllerInterface

class PessoaJuridicaCreatorController(PessoaJuridicaCreatorControllerInterface):
    def __init__(self, pessoa_juridica_repository: PessoaJuridicaRepositoryInterface) -> None:
        self.__pessoa_juridica_repository = pessoa_juridica_repository

    def create(self, pessoa_juridica_info: Dict) -> Dict:
        faturamento = pessoa_juridica_info["faturamento"]
        idade = pessoa_juridica_info["idade"]
        nome_fantasia = pessoa_juridica_info["nome_fantasia"]
        celular = pessoa_juridica_info["celular"]
        email_corporativo = pessoa_juridica_info["email_corporativo"]
        categoria = pessoa_juridica_info["categoria"]
        saldo = pessoa_juridica_info["saldo"]

        self.__validate_nome_fantasia(nome_fantasia)
        self.__insert_pessoa_juridica_in_db(faturamento,
                                            idade,
                                            nome_fantasia,
                                            celular,
                                            email_corporativo,
                                            categoria,
                                            saldo)

        formated_response = self.__format_response(pessoa_juridica_info)

        return formated_response

    def __validate_nome_fantasia(self, nome_fantasia) -> None:
        non_valid_caracteres = re.compile(r'[^a-zA-Z ]')

        if non_valid_caracteres.search(nome_fantasia):
            raise Exception("Nome fantasia inválido!")

    def __insert_pessoa_juridica_in_db(self,
                                        faturamento: float,
                                        idade: int,
                                        nome_fantasia: str,
                                        celular: str,
                                        email_corporativo: str,
                                        categoria: str,
                                        saldo: float) -> None:

        self.__pessoa_juridica_repository.insert_pessoa_juridica(faturamento,
                                                                 idade,
                                                                 nome_fantasia,
                                                                 celular,
                                                                 email_corporativo,
                                                                 categoria,
                                                                 saldo
                                                                )

    def __format_response(self, pessoa_juridica_info: PessoaJuridicaTable) -> Dict:
        return {
            "data": {
                "type": "Pessoa Jurídica",
                "count": 1,
                "attributes": pessoa_juridica_info
            }
        }
