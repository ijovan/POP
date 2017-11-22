from src.main.python.model.table import Table
from src.main.python.data_mapping.questions_mapper import QuestionsMapper


class Questions(Table):
    TABLE_NAME = "questions"
    MAPPER = QuestionsMapper
    HEADER = [
        "id", "owner_id", "is_answered", "view_count",
        "answer_count", "score", "last_activity_date",
        "creation_date", "last_edit_date", "link", "title",
        "bounty_user_id", "close_vote_count", "delete_vote_count",
        "down_vote_count", "favorite_count", "last_editor_id",
        "reopen_vote_count", "up_vote_count", "bounty_amount",
        "bounty_closes_date", "closed_date", "closed_reason",
        "locked_date", "accepted_answer_id"
    ]

    def load_period(self, params):
        items = self.MAPPER.load_period(params)

        self.insert_list(items)

    def users(self):
        return list(item['owner_id'] for item in self._rows())

    def tags(self):
        transform_tag = lambda item, tag_id: {
           'question_id': item['id'],
           'tag_id': tag_id
        }

        transform_tags = lambda item: \
            list(transform_tag(item, tag_id) for tag_id in item['tag_ids'])

        items_tags = list(map(transform_tags, self._rows()))

        return [tag for item_tags in items_tags for tag in item_tags]
