import errors as errors
from controllers.base import BaseController
from request import Request
from response import Response


class Router:
    def __init__(self):
        self.routes = {
            'get': [],
            'post': []
        }

    def add(self, http_method: str, uri: str, ctrl: BaseController, ctrl_method: str):
        self.routes[http_method].append(
            {
                'uri': uri,
                'ctrl': ctrl,
                'ctrl_method': ctrl_method
            }
        )

    def get(self, *args):
        self.add('get', *args)

    def post(self, *args):
        self.add('post', *args)

    def run(self, request: Request, response: Response):
        http_method = request.method.lower()    # post
        method_routes = self.routes[http_method]    # [{'uri': 'some_uri', 'ctrl': Ctrl. 'ctrl_method': 'home'}]

        route = None
        for r in method_routes:
            if r['uri'] == request.uri:
                route = r
                break

        print(route)
        if not route:
            return errors.not_found(request, response)

        try:
            ctrl = route['ctrl'](request, response)
            getattr(ctrl, route['ctrl_method'])()

        except BaseException as e:
            print(e)
            return errors.internal_server_error(request, response)
