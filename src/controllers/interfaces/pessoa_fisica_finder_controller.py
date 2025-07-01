from typing import Dict
from abc import ABC, abstractmethod

class PessoaFisicaFinderControllerInterface(ABC):
    
    @abstractmethod
    def find(self, pessoa_fisica_id: int) -> Dict:
        pass