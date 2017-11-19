import json


class MockHttpClient:
    @classmethod
    def get(cls, entity):
        return json.load(open('fixtures/client_response.json'))
