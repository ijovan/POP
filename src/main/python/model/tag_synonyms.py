from src.main.python.model.table import Table
from src.main.python.data_mapping.tag_synonyms_mapper import TagSynonymsMapper


class TagSynonyms(Table):
    TABLE_NAME = "tag_synonyms"
    MAPPER = TagSynonymsMapper
    HEADER = [
        "to_tag", "from_tag", "applied_count", "creation_date", "last_applied_date"
    ]

    def _id(self, item):
        return f"{item['to_tag']}&{item['from_tag']}"

    def resolve_all(self):
        tag_ids = list(self.repository.tags.items.keys())

        tag_synonyms = __class__._map_chunks(tag_ids, 20,
            lambda chunk: self.MAPPER.load(chunk)
        )

        self.insert_list(tag_synonyms)
