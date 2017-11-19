from src.main.python.configuration import Configuration
from src.main.python.http_client import HttpClient
from src.main.python.mock_http_client import MockHttpClient

class DataMapper:
    def __init__(self, table):
        self.table = table

    def _http_client(self):
        client_class = Configuration().values['api_client']

        return globals()[client_class]
