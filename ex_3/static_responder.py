from glob import glob
import os
from request import Request
from response import Response


class StaticResponder:
    def __init__(self, request: Request, response: Response, static_dir: str) -> None:
        self.request = request
        self.response = response
        self.static_dir = static_dir
        self.file = None
        self._check_file()

    def _check_file(self):
        path = './' + self.static_dir + self.request.uri
        # path = ./     static          /styles.css

        files: list[str] = glob(path)

        if len(files) > 0 and os.path.isfile(files[0]):
            self.file = files[0]

    def prepare_response(self):
        if self.file:
            file = open(self.file, 'rb')
            self.response.set_file_body(file)
