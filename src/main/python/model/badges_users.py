from src.main.python.model.table import Table
from src.main.python.data_mapping.badges_users_mapper import BadgesUsersMapper


class BadgesUsers(Table):
    TABLE_NAME = "badges_users"
    MAPPER = BadgesUsersMapper
    HEADER = ["badge_id", "user_id"]

    def _id(self, item):
        return f"{item['badge_id']}&{item['user_id']}"

    def resolve_all(self):
        user_ids = list(self.repository.users.items.keys())

        badges_users = []
        chunk_index = 1

        for chunk in self.__class__._chunks(user_ids, 100):
            print(f"Fetching chunk {chunk_index}...")

            chunk_index += 1
            badges_users += self.MAPPER.load(chunk)

        self.insert_list(badges_users)
