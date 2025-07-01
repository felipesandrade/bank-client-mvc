from typing import Dict
from abc import ABC, abstractmethod

class PessaoJuridicaFinderControllerInterface(ABC):

    @abstractmethod
    def find(self, pessoa_juridica_id: int) -> Dict:
        pass
