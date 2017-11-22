from src.main.python.data_mapping.data_mapper import DataMapper
from src.main.python.request import Request


class TagSynonymsMapper(DataMapper):
    @classmethod
    def load(cls, ids):
        request = Request({
            'entity': 'tags',
            'ids': ids,
            'submethod': 'synonyms'
        })

        return request.items()
