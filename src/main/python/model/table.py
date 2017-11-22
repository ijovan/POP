from src.main.python.csv import CSV
import os


class Table:
    TABLE_NAME = ""
    HEADER = []
    MAPPER = None

    def __init__(self, repository):
        self.items = {}
        self.repository = repository
        self._key_cache = self._load_key_cache()

    def insert_list(self, items):
        for item in items:
            self.insert(item)

    def insert(self, item):
        if str(self._id(item)) in self._key_cache:
            return

        if self._id(item) not in list(self.items.keys()):
            self.items[self._id(item)] = item
        elif self.items[self._id(item)] is None:
            self.items[self._id(item)] = item

    def commit(self):
        keys = list(self.items.keys())
        values = list(self.items.values())

        rows = list(self.__item_to_row(item) for item in values)

        if os.path.isfile(self.__file_path()):
            CSV.append(self.__file_path(), rows)
        else:
            CSV.write(self.__file_path(), [self.HEADER] + rows)

        self.items = {}
        self._key_cache += keys

        CSV.write(self.__key_cache_path(), [self._key_cache])

    def _rows(self):
        return list(self.items.values())

    def _id(self, item):
        return item['id']

    @staticmethod
    def _map_chunks(_list, chunk_size, function):
        chunks = list(map(
            lambda index: _list[index:index+chunk_size],
            range(0, len(_list), chunk_size)
        ))
        chunk_index = 1
        output = []

        for chunk in chunks:
            print(f"Processing chunk {chunk_index}/{len(chunks)}...")
            chunk_index += 1
            output += function(chunk)

        return output

    def _load_key_cache(self):
        path = self.__key_cache_path()

        if os.path.isfile(self.__key_cache_path()):
            return CSV.read(path)[0]
        else:
            return []

    def __item_to_row(self, item):
        return list(item.get(key, "") for key in self.HEADER)

    def __file_path(self):
        return f"{self.repository.STORE_PATH}/{self.TABLE_NAME}.csv"

    def __key_cache_path(self):
        return f"{self.repository.KEY_CACHE_PATH}/{self.TABLE_NAME}.csv"
