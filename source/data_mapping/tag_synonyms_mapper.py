from source.data_mapping.data_mapper import DataMapper
from source.resource import Resource


class TagSynonymsMapper(DataMapper):
    CHUNK_SIZE = 20

    @classmethod
    def load_from_tags(cls, tag_ids):
        def load_chunk(chunk):
            return Resource({
                'entity': 'tags',
                'ids': chunk,
                'submethod': 'synonyms'
            }).items()

        return cls._map_chunks(tag_ids, load_chunk)
