from src.main.python.repository import Repository
from datetime import date


class Period:
    DEFAULT_DEPTH = 1

    @staticmethod
    def year(year):
        return [date(year, 1, 1), date(year, 12, 31)]

    def __init__(self, start_date, end_date, depth=None):
        self.repository = Repository()
        self.start_date = start_date
        self.end_date = end_date
        self.depth = depth or self.DEFAULT_DEPTH

    def pull(self):
        self.repository.questions.load_period({
            'from': self.start_date,
            'to': self.end_date,
            'max_depth': self.depth
        })

        self.repository.resolve()
        self.repository.commit()
