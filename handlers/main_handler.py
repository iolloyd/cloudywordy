from tornado.web import RequestHandler
from tornado.escape import json_decode
from lib.grabber import save_top_words


class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello, world")

    def post(self):
        data = json_decode(self.request.body)
        url = data['url']
        save_top_words(url)
        self.redirect('/urls')
