from src.main.python.credentials import Credentials
from src.main.python.repository import Repository
from src.main.python.period import Period
from datetime import date
import time
import sys


DEPTH = 1


def check_credentials():
    if not Credentials.key() or not Credentials.access_token():
        Credentials.print_warning()
        sys.exit()


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


check_credentials()

load_periods(Repository(), [
    year_period(2016)
])
