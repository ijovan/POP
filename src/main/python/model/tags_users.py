from src.main.python.model.table import Table
from src.main.python.data_mapping.tags_users_mapper import TagsUsersMapper


class TagsUsers(Table):
    TABLE_NAME = "tags_users"
    MAPPER = TagsUsersMapper
    HEADER = ["tag_id", "user_id", "count"]

    def _id(self, item):
        return f"{item['tag_id']}&{item['user_id']}"

    def resolve_all(self):
        user_ids = list(self.repository.users.items.keys())

        tags_users = []
        chunk_index = 1

        for chunk in self.__class__._chunks(user_ids, 100):
            print(f"Fetching chunk {chunk_index}...")

            chunk_index += 1
            tags_users += self.MAPPER.load('users', chunk)

        self.insert_list(tags_users)
