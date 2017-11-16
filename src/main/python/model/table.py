from src.main.python.csv import CSV


class Table:
    TABLE_NAME = ""
    HEADER = []

    def __init__(self, repository):
        self.items = {}
        self.repository = repository

    def insert_list(self, items):
        for item in items:
            self.insert(item)

    def insert(self, item):
        if self._id(item) not in list(self.items.keys()):
            self.items[self._id(item)] = item

    def commit(self):
        values = list(self.items.values())

        rows = list(self.__item_to_row(item) for item in values)
        table = [self.HEADER] + rows

        CSV.write(self.__file_path(), table)

    def _id(self, item):
        return item['id']

    def __item_to_row(self, item):
        return list(item.get(key, "") for key in self.HEADER)

    def __file_path(self):
        return f"{self.repository.store_path}/{self.TABLE_NAME}.csv"
