from source.data_mapping.data_mapper import DataMapper
from source.resource import Resource


class TagsMapper(DataMapper):
    REQUEST_FILTER = '!9YdnSC5td'
    CHUNK_SIZE = 20

    @classmethod
    def load(cls, ids):
        def load_chunk(chunk):
            return Resource({
                'entity': 'tags',
                'ids': chunk,
                'submethod': 'info',
                'query_params': {'filter': cls.REQUEST_FILTER}
            }).items()

        tags = cls._map_chunks(ids, load_chunk)

        return list(map(cls.tag, tags))

    @staticmethod
    def tag(tag):
        tag['id'] = tag['name']

        return tag
