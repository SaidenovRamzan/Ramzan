import socketserver
from controllers.pages import PagesController
from controllers.posts import PostsController
from request import Request
from response import Response
from router import Router
from static_responder import StaticResponder
import errors as errors
from problems import Problems
import time 

HOST, PORT = '127.0.0.1', 1026

# CRUDL - Create, Read, Update, Delete, List
# /posts
# GET - /posts
# GET - /posts/{id}
# POST - /posts
# PUT/PATCH - /posts/{id}
# DELETE - /posts/{id}


router = Router()
router.get('/', PagesController, 'home')
router.get('/about-us', PagesController, 'about_us')
router.get('/posts', PostsController, 'get_list')
router.post('/posts', PostsController, 'create')


class MyTCPHandler(socketserver.StreamRequestHandler):
    def handle(self) -> None:
        request = Request(file=self.rfile)
        response = Response(file=self.wfile)
        problem = Problems(request, response)
        router.run(request, response)

        print(
            f'Method: {request.method}\n'
            f'URI: {request.uri}\n'
            f'Protocol: {request.protocol}\n'
        )
        problem.poblem()
        
        response.send()
        


socketserver.TCPServer.allow_reuse_address = True


with socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler) as server:
    server.serve_forever()
