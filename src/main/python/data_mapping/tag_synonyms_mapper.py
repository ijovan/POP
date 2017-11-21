from src.main.python.data_mapping.data_mapper import DataMapper


class TagSynonymsMapper(DataMapper):
    @classmethod
    def load(cls, ids):
        return cls._http_client().get('tags', ids, 'synonyms')
