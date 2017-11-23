from src.main.python.csv_file import CSVFile


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
        _id = self.item_id(item)

        if (not self.items.get(_id) and _id not in self._key_cache):
            self.items[_id] = item

    def commit(self):
        keys = list(self.items.keys())
        values = list(self.items.values())
        rows = list(self.__item_to_row(item) for item in values)

        table_file = CSVFile(self.__file_path())

        if table_file.exists():
            table_file.append(rows)
        else:
            table_file.write([self.HEADER] + rows)

        self.items = {}
        self._key_cache += keys

        CSVFile(self.__key_cache_path()).write([self._key_cache])

    @staticmethod
    def item_id(item):
        return str(item['id'])

    def rows(self):
        return list(self.items.values())

    def _load_key_cache(self):
        key_cache_file = CSVFile(self.__key_cache_path())

        if key_cache_file.exists():
            return key_cache_file.read()[0]
        else:
            return []

    def __item_to_row(self, item):
        return list(item.get(key, "") for key in self.HEADER)

    def __file_path(self):
        return f"{self.repository.STORE_PATH}/{self.TABLE_NAME}.csv"

    def __key_cache_path(self):
        return f"{self.repository.KEY_CACHE_PATH}/{self.TABLE_NAME}.csv"
