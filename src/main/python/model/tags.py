from src.main.python.model.table import Table
from src.main.python.data_mapping.tags_mapper import TagsMapper


class Tags(Table):
    TABLE_NAME = "tags"
    MAPPER = TagsMapper
    HEADER = [
        "id", "count", "has_synonyms", "is_moderator_only", "is_required",
        "last_activity_date"
    ]

    def resolve_all(self):
        ids = list(map(
            lambda tag_question: tag_question['tag_id'],
            self.repository.questions.tags()
        ))

        tags = self.MAPPER.load(ids)

        self.insert_list(tags)
