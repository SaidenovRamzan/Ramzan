import urllib.parse
from typing import BinaryIO


class Request:
    def __init__(self, file: BinaryIO) -> None:
        self.file = file
        self.body = self.method = self.uri = self.protocol = ''
        self.headers = {}

        self.parse_request_line()
        self.parse_headers()
        self.parse_body()

    def readline(self):
        return self.file.readline().decode().strip()

    def parse_request_line(self) -> None:
        request_line = self.readline()

        self.method, self.uri, self.protocol = request_line.split()

    def parse_headers(self) -> None:
        while True:
            header = self.readline()

            if not header:
                break

            header_name, header_value = header.split(': ')
            self.headers[header_name] = header_value

    def parse_body(self) -> None:
        if 'Content-Length' in self.headers:
            content_length = int(self.headers['Content-Length'])
            body = self.file.read(content_length)

            if isinstance(body, bytes):
                decoded = body.decode()
                parsed = urllib.parse.parse_qs(decoded)

                for k, v in parsed.items():
                    parsed[k] = ' '.join(v)     # noqa

                self.body = parsed

            else:
                self.body = self.file.read(content_length)
