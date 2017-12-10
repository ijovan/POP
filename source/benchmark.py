import time


class Benchmark:
    def __init__(self, name):
        self.start_time = time.time()
        self.name = name

        print(f"{self.name} starting...")

    def print_current(self):
        duration = time.time() - self.start_time

        print(f"{self.name} took {'%.2f' % duration}s.")
