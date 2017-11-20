from src.main.python.configuration import Configuration
from src.main.python.http_client import HttpClient
from src.main.python.mock_http_client import MockHttpClient

class DataMapper:
    def _http_client():
        client_class = Configuration().values['api_client']

        return globals()[client_class]
