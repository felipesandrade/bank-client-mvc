from typing import Dict

class HttpRequest:
    def __init__(self, status_code: int, body: Dict = None) -> None:
        self.status_code = status_code
        self.body = body
