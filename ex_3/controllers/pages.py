from .base import BaseController


class PagesController(BaseController):
    def home(self):
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body('<h1>This is homepage</h1>')

    def about_us(self):
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body('<h1>This is about us page</h1>')
