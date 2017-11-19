from src.main.python.data_mapper import DataMapper


class TagsMapper(DataMapper):
    def load(self, ids):
        tags = self._http_client().get('tags', ids, 'info')['items']

        for tag in tags:
            tag['id'] = tag['name']

            del tag['name']

            self.table.insert(tag)
