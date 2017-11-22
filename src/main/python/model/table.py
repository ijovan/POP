from src.main.python.csv import CSV


class Table:
    TABLE_NAME = ""
    HEADER = []
    MAPPER = None

    def __init__(self, repository):
        self.items = {}
        self.repository = repository

    def insert_list(self, items):
        for item in items:
            self.insert(item)

    def insert(self, item):
        if self._id(item) not in list(self.items.keys()):
            self.items[self._id(item)] = item
        elif self.items[self._id(item)] is None:
            self.items[self._id(item)] = item

    def load_all(self):
        items = self.MAPPER.load_all()

        self.insert_list(items)

    def commit(self):
        keys = list(self.items.keys())
        values = list(self.items.values())

        rows = list(self.__item_to_row(item) for item in values)
        table = [self.HEADER] + rows

        CSV.write(self.__file_path(), table)
        CSV.write(self.__key_cache_path(), [keys])

    def _rows(self):
        return list(self.items.values())

    def _id(self, item):
        return item['id']

    def _map_chunks(_list, chunk_size, function):
        chunks = list(map(
            lambda index: _list[index : index + chunk_size],
            range(0, len(_list), chunk_size)
        ))
        chunk_index = 1
        output = []

        for chunk in chunks:
            print(f"Processing chunk {chunk_index}/{len(chunks)}...")
            chunk_index += 1
            output += function(chunk)

        return output

    def __item_to_row(self, item):
        return list(item.get(key, "") for key in self.HEADER)

    def __file_path(self):
        return f"{self.repository.store_path}/{self.TABLE_NAME}.csv"

    def __key_cache_path(self):
        return f"{self.repository.key_cache_path}/{self.TABLE_NAME}.csv"
