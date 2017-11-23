from source.benchmark import Benchmark
from source.period import Period


# Time periods from which to pull questions.
PERIODS = [
    Period.year(2016)
]

# How deep to go when pullinq questions from a period.
# One depth level equals 100 questions.
DEPTH = 1


benchmark_total = Benchmark("Total")

for period in PERIODS:
    benchmark_period = Benchmark("Period")

    Period(*period, DEPTH).pull()

    benchmark_period.print_current()

benchmark_total.print_current()
