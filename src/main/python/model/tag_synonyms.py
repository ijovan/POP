from src.main.python.model.table import Table
from src.main.python.data_mapping.tag_synonyms_mapper import TagSynonymsMapper


class TagSynonyms(Table):
    TABLE_NAME = "tag_synonyms"
    MAPPER = TagSynonymsMapper
    HEADER = [
        "to_tag", "from_tag", "applied_count", "creation_date",
        "last_applied_date"
    ]

    def item_id(self, item):
        return f"{item['to_tag']}&{item['from_tag']}"

    def resolve_all(self):
        tag_ids = list(self.repository.tags.items.keys())

        tag_synonyms = self.MAPPER.load_from_tags(tag_ids)

        self.insert_list(tag_synonyms)
