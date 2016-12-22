from tornado.web import RequestHandler
from lib import get_data_from_cloudsql


class AdminHandler(RequestHandler):
    def get(self):
        counts = dict(get_data_from_cloudsql())
        self.render('../templates/admin.html', counts=counts)
