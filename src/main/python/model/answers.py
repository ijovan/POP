from src.main.python.model.table import Table
from src.main.python.data_mapping.answers_mapper import AnswersMapper


class Answers(Table):
    TABLE_NAME = "answers"
    MAPPER_CLASS = AnswersMapper
    HEADER = [
        "id", "owner_id", "question_id", "is_accepted", "score",
        "last_activity_date", "last_edit_date", "creation_date"
    ]

    def resolve_all(self):
        question_ids = self.repository.questions.items.keys()

        self.mapper.load(question_ids)

    def users(self):
        return list(item['owner_id'] for item in self._rows())
