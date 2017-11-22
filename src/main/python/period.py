class Period:
    def __init__(self, repository, start_date, end_date, depth):
        self.repository = repository
        self.start_date = start_date
        self.end_date = end_date
        self.depth = depth

    def load(self):
        self.repository.questions.load_period({
            'from': self.start_date,
            'to': self.end_date,
            'max_depth': self.depth
        })

        self.repository.resolve()
        self.repository.commit()
