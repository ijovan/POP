from src.main.python.data_mapping.data_mapper import DataMapper
from src.main.python.request import Request


class TagsMapper(DataMapper):
    REQUEST_FILTER = '!9YdnSC5td'

    @classmethod
    def load(cls, ids):
        request = Request({
            'entity': 'tags',
            'ids': ids,
            'submethod': 'info',
            'query_params': {'filter': cls.REQUEST_FILTER}
        })

        tags = request.items()

        for tag in tags:
            tag['id'] = tag.pop('name')

        return tags
