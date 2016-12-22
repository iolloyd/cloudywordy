from tornado.web import RequestHandler
from lib.grabber import save_top_words
import urllib


class MainHandler(RequestHandler):
    def get(self):
        self.render('../templates/form.html')

    def post(self):
        url = self.get_argument('url')
        print('saving')
        save_top_words(url)
        print('saved')
        self.redirect('/')
