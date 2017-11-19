from src.main.python.model.table import Table
from src.main.python.tags_mapper import TagsMapper


class Tags(Table):
    TABLE_NAME = "tags"
    MAPPER_CLASS = TagsMapper
    HEADER = [
        "id", "count", "has_synonyms", "is_moderator_only", "is_required"
    ]

    def resolve_all(self):
        ids = list(map(
            lambda tag_question: tag_question['tag_id'],
            self.repository.questions.tags()
        ))

        self.mapper.load(ids)
