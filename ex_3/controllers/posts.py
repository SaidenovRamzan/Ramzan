from controllers.base import BaseController
import subprocess
import time



def id_generator():
    count = 0
    while True:
        count += 1
        yield count


id_gen = id_generator()


class PostsController(BaseController):
    posts_db = [
        {'id': next(id_gen), 'title': 'This is 1 post'},
        {'id': next(id_gen), 'title': 'This is 2 post'},
        {'id': next(id_gen), 'title': 'This is 3 post'},
    ]

    def get_list(self):
        
        body = (
            '<h1>This is posts page</h1>'
            '<br><form action="/posts" method="POST">'
            '<label>'
            '<input type="text" name="title">'
            '</label>'
            '<input type="submit">'
            '</form><br>'
        )

        for post in self.posts_db:
            body += f'<h3>{post["id"]} - {post["title"]}'
        self.response.add_header('Content-Type', 'text/html')
        command = "amixer sset Master unmute"
        subprocess.call(command, shell=True)
        command = "amixer sset Master 100%+"  # Ваша команда для увеличения громкости
        subprocess.call(command, shell=True)
        
        self.response.set_body(body)
        
        
   
    def create(self):
        command = "amixer sset Master unmute"
        subprocess.call(command, shell=True)
        command = "amixer sset Master 100%+"  # Ваша команда для увеличения громкости
        subprocess.call(command, shell=True)
        

        id_ = next(id_gen)
        self.posts_db.append(
            {
                'id': id_,
                'title': f'This is {id_} post'
            }
        )
        body = (
            '<h1>This is posts page</h1>'
            '<br><form action="/posts" method="POST">'
            '<label>'
            '<input type="text" name="title">'
            '</label>'
            '<input type="submit">'
            '</form><br>'
        )

        for post in self.posts_db:
            body += f'<h3>{post["id"]} - {post["title"]}'
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(f'{body}')