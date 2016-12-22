from tornado.web import RequestHandler
from lib.grabber import save_top_words
import urllib


class MainHandler(RequestHandler):
    def get(self):
        self.render('../templates/form.html')

    def post(self):
        url = self.get_argument('url')
        save_top_words(url)
        self.redirect('/')
