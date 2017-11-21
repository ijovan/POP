from src.main.python.data_mapping.data_mapper import DataMapper


class TagsMapper(DataMapper):
    REQUEST_FILTER = '!9YdnSC5td'

    @classmethod
    def load(cls, ids):
        tags = cls._http_client().get(
            'tags',
            ids,
            'info',
            {'filter': cls.REQUEST_FILTER}
        )

        for tag in tags:
            tag['id'] = tag['name']

            del tag['name']

        return tags
