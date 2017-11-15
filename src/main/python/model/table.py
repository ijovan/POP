from src.main.python.csv import CSV


class Table:
    TABLE_NAME = ""
    HEADER = []

    @classmethod
    def insert(cls, items):
        rows = list(cls.item_to_row(item) for item in items)
        table = [cls.HEADER] + rows

        CSV.write(f"{cls.TABLE_NAME}.csv", table)

    @classmethod
    def item_to_row(cls, item):
        return list(item.get(key, "") for key in cls.HEADER)
