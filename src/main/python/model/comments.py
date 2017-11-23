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

        comments = self._merge_groups([
            self.MAPPER.load_from_parents('answers', answer_ids),
            self.MAPPER.load_from_parents('questions', question_ids)
        ])

        self.insert_list(list(comments.values()))

    def users(self):
        return list(item['owner_id'] for item in self.rows())

    @staticmethod
    def _merge_groups(groups):
        items = {}

        for group in groups:
            for item in group:
                key = item['id']

                if key not in list(items.keys()):
                    items[key] = item

        return items
