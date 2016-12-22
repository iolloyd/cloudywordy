import tornado.ioloop
import tornado.web
from handlers import MainHandler, AdminHandler


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/admin", AdminHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

