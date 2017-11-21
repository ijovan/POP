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

        answer_comments = []
        chunk_index = 1

        for chunk in self.__class__._chunks(answer_ids, 100):
            print(f"Fetching chunk {chunk_index}...")

            chunk_index += 1
            answer_comments += \
                self.MAPPER.load('answers', chunk)

        question_comments = []
        chunk_index = 1

        for chunk in self.__class__._chunks(question_ids, 100):
            print(f"Fetching chunk {chunk_index}...")

            chunk_index += 1
            question_comments += \
                self.MAPPER.load('questions', chunk)

        comments = {}

        for comments_group in [answer_comments, question_comments]:
            for comment in comments_group:
                key = comment['id']

                if key not in list(comments.keys()):
                    comments[key] = comment

        self.insert_list(list(comments.values()))

    def users(self):
        return list(item['owner_id'] for item in self._rows())
