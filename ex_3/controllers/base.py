from request import Request
from response import Response


class BaseController:
    def __init__(self, request: Request, response: Response):
        self.request = request
        self.response = response
