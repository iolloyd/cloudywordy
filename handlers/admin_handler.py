from tornado.web import RequestHandler
from lib import get_data_from_cloudsql
from lib.cryption import decrypt_word


class AdminHandler(RequestHandler):
    def get(self):
        counts = get_data_from_cloudsql()
        counts = [(decrypt_word(x[0]), x[1]) for x in counts]
        print(counts)
        self.render('../templates/admin.html', counts=counts)
