from source.repository import Repository
from datetime import date


class Period:
    DEFAULT_DEPTH = 1

    def year(year, depth=None):
        return Period(date(year, 1, 1), date(year + 1, 1, 1), depth)

    def year_month(year, month, depth=None):
        return Period(
            date(year, month, 1),
            date(year + month // 12, month % 12 + 1, 1),
            depth
        )

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
