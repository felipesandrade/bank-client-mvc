from typing import List
from abc import ABC, abstractmethod

class PessoaJuridicaRepositoryInterface(ABC):
    @abstractmethod
    def insert_pessoa_jurifica(self,
                                faturamento: float,
                                idade: int,
                                nome_fantasia: str,
                                celular: str,
                                email_corporativo: str,
                                categoria: str,
                                saldo: float
                                 ) -> None:
        pass

    @abstractmethod
    def list_pessoa_juridica(self) -> List:
        pass

    @abstractmethod
    def delete_pessoa_juridica(self, pessoa_juridica_id: int) -> None:
        pass
