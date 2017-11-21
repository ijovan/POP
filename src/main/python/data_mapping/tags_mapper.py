from src.main.python.data_mapping.data_mapper import DataMapper


class TagsMapper(DataMapper):
    @classmethod
    def load(cls, ids):
        tags = cls._http_client().get('tags', ids, 'info')

        for tag in tags:
            tag['id'] = tag['name']

            del tag['name']

        return tags
