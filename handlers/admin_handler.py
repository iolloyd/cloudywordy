from tornado.web import RequestHandler
from lib import get_data_from_cloudsql


class AdminHandler(RequestHandler):
    def get(self):
        data = get_data_from_cloudsql()

        return data
