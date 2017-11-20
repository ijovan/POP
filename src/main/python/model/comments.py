from src.main.python.model.table import Table
from src.main.python.data_mapping.comments_mapper import CommentsMapper


class Comments(Table):
    TABLE_NAME = "comments"
    MAPPER_CLASS = CommentsMapper
    HEADER = [
        "id", "owner_id", "post_id", "reply_to_user_id", "edited",
        "score", "creation_date"
    ]

    def resolve_all(self):
        question_ids = self.repository.questions.items.keys()
        answers_ids = self.repository.answers.items.keys()

        self.mapper.load('questions', question_ids)
        self.mapper.load('answers', answers_ids)

    def users(self):
        return list(item['owner_id'] for item in self._rows())
