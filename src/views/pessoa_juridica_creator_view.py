from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface
from src.controllers.interfaces.pessoa_juridica_creator_controller import PessoaJuridicaCreatorControllerInterface

class PessoaJuridicaCreatorView(ViewInterface):
    def __init__(self, controller: PessoaJuridicaCreatorControllerInterface) -> None:
        self.__controller= controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pessoa_juridica_info = http_request.body
        body_response = self.__controller.create(pessoa_juridica_info)

        return HttpResponse(status_code=201, body=body_response)
