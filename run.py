from src.main.python.repository import Repository
from src.main.python.configuration import Configuration
from datetime import date


def pull_questions():
    repository = Repository()

    periods = [
        year_period(2015),
        year_period(2016),
        year_period(2017)
    ]

    for start, end in periods:
        repository.questions.load_period(
            {'from': start, 'to': end, 'depth': 5}
        )
        repository.resolve()
        repository.commit()

def year_period(year):
    return [date(year, 1, 1), date(year, 12, 31)]

Configuration().set_prod_environment()
pull_questions()
