from src.main.python.data_mapping.data_mapper import DataMapper
from src.main.python.resource import Resource


class TagsMapper(DataMapper):
    REQUEST_FILTER = '!9YdnSC5td'

    @classmethod
    def load(cls, ids):
        resource = Resource({
            'entity': 'tags',
            'ids': ids,
            'submethod': 'info',
            'query_params': {'filter': cls.REQUEST_FILTER}
        })

        tags = resource.items()

        for tag in tags:
            tag['id'] = tag.pop('name')

        return tags
