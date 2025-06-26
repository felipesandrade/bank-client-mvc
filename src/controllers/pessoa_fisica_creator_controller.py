import re
from typing import Dict
from src.models.sqlite.interfaces.pessoa_fisica_repository import PessoaFisicaRepositoryInterface

class PessoaFisicaCreatorController:
    def __init__(self, pessoa_fisica_repository: PessoaFisicaRepositoryInterface) -> None:
        self.__pessoa_fisica_repository = pessoa_fisica_repository

    # O pessoa_fisica_info é uma informação que virá do protocolo HTTP
    def create(self, pessoa_fisica_info: Dict) -> Dict:
        renda_mensal = pessoa_fisica_info["renda_mensal"]
        idade = pessoa_fisica_info["idade"]
        nome_completo = pessoa_fisica_info["nome_completo"]
        celular = pessoa_fisica_info["celular"]
        email = pessoa_fisica_info["email"]
        categoria = pessoa_fisica_info["categoria"]
        saldo = pessoa_fisica_info["saldo"]

        self.__validate_nome_completo(nome_completo)
        self.__insert_pessoa_fisica_in_db(renda_mensal,
                                          idade,
                                          nome_completo,
                                          celular,
                                          email,
                                          categoria,
                                          saldo)
        formated_response = self.__format_response(pessoa_fisica_info)

        return formated_response


    def __validate_nome_completo(self, nome_completo: str) -> None:
        # Expressão regular para caracteres que não são letras
        non_valid_caracteres = re.compile(r'[^a-zA-Z ]')

        if non_valid_caracteres.search(nome_completo):
            raise Exception("Nome completo inválido!")

    def __insert_pessoa_fisica_in_db(self,
                                    renda_mensal: float,
                                    idade: int,
                                    nome_completo: str,
                                    celular: str,
                                    email: str,
                                    categoria: str,
                                    saldo: float) -> None:
        
        self.__pessoa_fisica_repository.insert_pessoa_fisica(renda_mensal,
                                                             idade,
                                                             nome_completo,
                                                             celular,
                                                             email,
                                                             categoria,
                                                             saldo)

    def __format_response(self, pessoa_fisica_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Pessoa Física",
                "count": 1,
                "attributes": pessoa_fisica_info 
            }
        }
