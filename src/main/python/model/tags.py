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
        tag_id = lambda entity: entity['tag_id']

        ids_from_questions = list(map(
            tag_id, self.repository.tags_questions.items.values()
        ))

        ids_from_users = list(map(
            tag_id, self.repository.tags_users.items.values()
        ))

        ids = list(
            set(ids_from_questions) |
            set(ids_from_users)
        )

        tags = []
        chunk_index = 1

        for chunk in self.__class__._chunks(ids, 20):
            print(f"Fetching chunk {chunk_index}...")

            chunk_index += 1
            tags += self.MAPPER.load(chunk)

        self.insert_list(tags)
