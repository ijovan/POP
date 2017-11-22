from src.main.python.repository import Repository
from src.main.python.period import Period
from datetime import date
import time


DEPTH = 1


def load_periods(repository, periods):
    total_start_time = time.time()

    for start, end in periods:
        period_start_time = time.time()

        Period(repository, start, end, DEPTH).load()

        print_duration("Period", time.time(), period_start_time)

    print_duration("Total", time.time(), total_start_time)


def print_duration(name, end_time, start_time):
    print(f"{name} took {str(end_time - start_time)}s.")


def year_period(year):
    return [date(year, 1, 1), date(year, 12, 31)]


load_periods(Repository(), [
    year_period(2016)
])
