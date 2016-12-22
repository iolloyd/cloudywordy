import tornado
import tornado.ioloop
import tornado.web
from handlers import MainHandler, AdminHandler


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/submit", MainHandler),
        (r"/admin", AdminHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(9888)
    tornado.ioloop.IOLoop.current().start()

