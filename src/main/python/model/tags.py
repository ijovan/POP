from src.main.python.model.table import Table


class Tags(Table):
    TABLE_NAME = "tags"
    HEADER = ["name"]

    def _id(self, item):
        return item['name']
