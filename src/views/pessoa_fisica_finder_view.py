from src.controllers.interfaces.pessoa_fisica_finder_controller import PessoaFisicaFinderControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class PessoaFisicaFinderView(ViewInterface):
    def __init__(self, controller: PessoaFisicaFinderControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pessoa_fisica_id = http_request.param["pessoa_fisica_id"]
        body_response = self.__controller.find(pessoa_fisica_id)

        return HttpResponse(status_code=200 , body=body_response)
