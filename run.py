from src.main.python.credentials import Credentials
from src.main.python.period import Period
from src.main.python.benchmark import Benchmark


# Time periods from which to pull questions.
PERIODS = [
    Period.year(2016)
]

# How deep to go when pullinq questions from a period.
# One depth level equals 100 questions.
DEPTH = 1


benchmark_total = Benchmark("Total")

for start, end in PERIODS:
    benchmark_period = Benchmark("Period")

    # Pulls questions for a given period
    Period(start, end).pull()

    benchmark_period.print_current()

benchmark_total.print_current()
