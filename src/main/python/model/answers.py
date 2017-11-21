from src.main.python.model.table import Table
from src.main.python.data_mapping.answers_mapper import AnswersMapper


class Answers(Table):
    TABLE_NAME = "answers"
    MAPPER = AnswersMapper
    HEADER = [
        "id", "owner_id", "question_id", "is_accepted", "score",
        "last_activity_date", "last_edit_date", "creation_date",
        "awarded_bounty_amount", "down_vote_count", "last_editor_id",
        "link", "title", "up_vote_count"
    ]

    def resolve_all(self):
        question_ids = self.repository.questions.items.keys()

        questions = self.MAPPER.load(question_ids)

        self.insert_list(questions)

    def users(self):
        return list(item['owner_id'] for item in self._rows())
