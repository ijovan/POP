import json


class MockHttpClient:
    @classmethod
    def get(cls, entity, params_dict={}):
        return json.load(open('fixtures/client_response.json'))
