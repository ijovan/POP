from src.main.python.model.table import Table
from src.main.python.data_mapping.comments_mapper import CommentsMapper


class Comments(Table):
    TABLE_NAME = "comments"
    MAPPER = CommentsMapper
    HEADER = [
        "id", "owner_id", "post_id", "reply_to_user_id", "edited",
        "score", "creation_date", "link", "post_type"
    ]

    def resolve_all(self):
        answers_ids = self.repository.answers.items.keys()
        question_ids = self.repository.questions.items.keys()

        answer_comments = self.MAPPER.load('answers', answers_ids)
        question_comments = self.MAPPER.load('questions', question_ids)

        comments = {}

        for comments_group in [answer_comments, question_comments]:
            for comment in comments_group:
                key = comment['id']

                if key not in list(comments.keys()):
                    comments[key] = comment

        self.insert_list(list(comments.values()))

    def users(self):
        return list(item['owner_id'] for item in self._rows())
