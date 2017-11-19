from src.main.python.model.table import Table
from src.main.python.data_mapping.questions_mapper import QuestionsMapper


class Questions(Table):
    TABLE_NAME = "questions"
    MAPPER_CLASS = QuestionsMapper
    HEADER = [
        "id", "owner_id", "is_answered", "view_count",
        "answer_count", "score", "last_activity_date",
        "creation_date", "last_edit_date", "link", "title"
    ]

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
