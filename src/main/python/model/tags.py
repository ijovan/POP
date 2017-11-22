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
        def tag_id(entity): return entity['tag_id']

        ids_from_questions = list(map(
            tag_id, self.repository.tags_questions.items.values()
        ))

        ids_from_users = list(map(
            tag_id, self.repository.tags_users.items.values()
        ))

        parent_ids = list(
            set(ids_from_questions) |
            set(ids_from_users)
        )

        tags = self._map_chunks(parent_ids, 20,
            lambda chunk: self.MAPPER.load(chunk)
        )

        self.insert_list(tags)
