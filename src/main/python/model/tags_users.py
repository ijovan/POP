from src.main.python.model.table import Table
from src.main.python.data_mapping.tags_users_mapper import TagsUsersMapper


class TagsUsers(Table):
    TABLE_NAME = "tags_users"
    MAPPER_CLASS = TagsUsersMapper
    HEADER = ["tag_id", "user_id", "count"]

    def _id(self, item):
        return f"{item['tag_id']}&{item['user_id']}"

    def resolve_all(self):
        user_ids = list(self.repository.users.items.keys())

        self.mapper.load('users', user_ids)
