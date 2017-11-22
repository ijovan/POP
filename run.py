from src.main.python.repository import Repository
from datetime import date
import time


def pull_questions():
    repository = Repository()

    periods = [
        year_period(2016)
    ]

    total_start_time = time.time()

    for start, end in periods:
        period_start_time = time.time()

        repository.questions.load_period(
            {'from': start, 'to': end, 'max_depth': 1}
        )
        repository.resolve()
        repository.commit()

        period_end_time = time.time()

        print_duration(
            "Period downloading took", period_end_time, period_start_time
        )

    total_end_time = time.time()

    print_duration(
        "Complete downloading", total_end_time, total_start_time
    )

def print_duration(name, end_time, start_time):
    print(f"{name} took {str(end_time - start_time)} s.")

def year_period(year):
    return [date(year, 1, 1), date(year, 12, 31)]

pull_questions()
