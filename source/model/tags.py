from source.model.table import Table
from source.data_mapping.tags_mapper import TagsMapper


class Tags(Table):
    TABLE_NAME = "tags"
    MAPPER = TagsMapper
    HEADER = [
        "id", "name", "count", "has_synonyms", "is_moderator_only",
        "is_required", "last_activity_date"
    ]

    def resolve_all(self):
        def tag_id(entity): return entity['tag_id']

        ids_from_questions = set(map(
            tag_id, self.repository.tags_questions.items.values()
        ))
        ids_from_users = set(map(
            tag_id, self.repository.tags_users.items.values()
        ))

        parent_ids = ids_from_questions | ids_from_users
        missing_parent_ids = list(parent_ids - set(self._key_cache))

        tags = self.MAPPER.load(missing_parent_ids)

        self.insert_list(tags)
