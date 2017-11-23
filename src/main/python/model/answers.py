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
        question_ids = list(self.repository.questions.items.keys())

        answers = self._map_chunks(question_ids, 100,
            lambda chunk: self.MAPPER.load_from_questions(chunk)
        )

        self.insert_list(answers)

    def users(self):
        return list(item['owner_id'] for item in self.rows())
