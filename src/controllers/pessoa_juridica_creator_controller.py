from src.models.sqlite.interfaces.pessoa_juridica_repository import PessoaJuridicaRepositoryInterface

class PessoaJuridicaCreatorController:
    def __init__(self, pessoa_juridica_repository: PessoaJuridicaRepositoryInterface) -> None:
        self.__pessoa_juridica_repository = pessoa_juridica_repository
