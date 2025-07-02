from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface
from src.controllers.interfaces.pessoa_juridica_finder_controller import PessaoJuridicaFinderControllerInterface

class PessaoJuridicaFinderView(ViewInterface):
    def __init__(self, controller: PessaoJuridicaFinderControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pessoa_juridica_id = http_request.param["pessoa_juridica_id"]
        body_reponse = self.__controller.find(pessoa_juridica_id)

        return HttpResponse(status_code=200, body=body_reponse)
