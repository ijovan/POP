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
        values = list(self.items.values())

        rows = list(self.__item_to_row(item) for item in values)
        table = [self.HEADER] + rows

        CSV.write(self.__file_path(), table)

    def _rows(self):
        return list(self.items.values())

    def _id(self, item):
        return item['id']

    def _chunks(_list, n):
        for i in range(0, len(_list), n):
            yield _list[i:i + n]

    def __item_to_row(self, item):
        return list(item.get(key, "") for key in self.HEADER)

    def __file_path(self):
        return f"{self.repository.store_path}/{self.TABLE_NAME}.csv"
