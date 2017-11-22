from src.main.python.data_mapping.data_mapper import DataMapper
from src.main.python.resource import Resource


class TagSynonymsMapper(DataMapper):
    @classmethod
    def load_from_tags(cls, tag_ids):
        resource = Resource({
            'entity': 'tags',
            'ids': tag_ids,
            'submethod': 'synonyms'
        })

        return resource.items()
