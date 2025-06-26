from typing import List
from abc import ABC, abstractmethod
from src.models.sqlite.entities.pessoa_fisica import PessoaFisicaTable

class PessoaFisicaRepositoryInterface(ABC):
    @abstractmethod
    def insert_pessoa_fisica(self,
                             renda_mensal: float,
                             idade: int,
                             nome_completo: str,
                             celular: str,
                             email: str,
                             categoria: str,
                             saldo: float
                             ) -> None:
        pass

    @abstractmethod
    def list_pessoa_fisica(self) -> List[PessoaFisicaTable]:
        pass

    @abstractmethod
    def delete_pessoa_fisica(self, pessoa_fisica_id: int) -> None:
        pass
