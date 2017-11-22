from src.main.python.data_mapping.data_mapper import DataMapper
from src.main.python.resource import Resource


class TagSynonymsMapper(DataMapper):
    @classmethod
    def load(cls, ids):
        resource = Resource({
            'entity': 'tags',
            'ids': ids,
            'submethod': 'synonyms'
        })

        return resource.items()
