import json


class MockHttpClient:
    @classmethod
    def get(cls, entity, ids=[], submethod=None, params={}):
        return []
