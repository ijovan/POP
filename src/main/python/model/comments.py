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
        answer_ids = list(self.repository.answers.items.keys())
        question_ids = list(self.repository.questions.items.keys())

        answer_comments = self._map_chunks(answer_ids, 100,
            lambda chunk: self.MAPPER.load_from_parents('answers', chunk)
        )

        question_comments = self._map_chunks(question_ids, 100,
            lambda chunk: self.MAPPER.load_from_parents('questions', chunk)
        )

        comments = {}

        for comments_group in [answer_comments, question_comments]:
            for comment in comments_group:
                key = comment['id']

                if key not in list(comments.keys()):
                    comments[key] = comment

        self.insert_list(list(comments.values()))

    def users(self):
        return list(item['owner_id'] for item in self.rows())
