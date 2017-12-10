from source.benchmark import Benchmark
from source.period import Period


# How deep to go when pullinq questions from a period.
# One depth level equals 100 questions.
DEPTH = 1

# Time periods from which to pull questions.
YEARS = [2015, 2016, 2017]


benchmark_total = Benchmark("Total")

for year in YEARS:
    benchmark_year = Benchmark(f"Year: {year}")

    for month in range(1, 13):
        benchmark_month = Benchmark(f"Month: {month}")

        Period.year_month(year, month, DEPTH).pull()

        benchmark_month.print_current()

    benchmark_year.print_current()

benchmark_total.print_current()
