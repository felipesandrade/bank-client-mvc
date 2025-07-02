from typing import Dict

class HttpResponse:
    def __init__(self, body: Dict = None, param: Dict = None) -> None:
        self.body = body
        self.param = param
