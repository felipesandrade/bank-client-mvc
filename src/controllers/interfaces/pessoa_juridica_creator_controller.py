from typing import Dict
from abc import ABC, abstractmethod

class PessoaJuridicaCreatorControllerInterface(ABC):

    @abstractmethod
    def create(self, pessoa_juridica_info: Dict) -> Dict:
        pass
