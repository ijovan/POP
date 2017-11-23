from source.model.table import Table
from source.data_mapping.answers_mapper import AnswersMapper


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

        answers = self.MAPPER.load_from_questions(question_ids)

        self.insert_list(answers)

    def users(self):
        return list(item['owner_id'] for item in self.rows())
