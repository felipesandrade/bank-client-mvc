from typing import Dict
from abc import ABC, abstractmethod

class PessoaFisicaCreatorControllerInterface(ABC):

    @abstractmethod
    def create(self, pessoa_fisica_info: Dict) -> Dict:
        pass
