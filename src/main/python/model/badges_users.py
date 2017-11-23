from src.main.python.model.table import Table
from src.main.python.data_mapping.badges_users_mapper import BadgesUsersMapper


class BadgesUsers(Table):
    TABLE_NAME = "badges_users"
    MAPPER = BadgesUsersMapper
    HEADER = ["badge_id", "user_id"]

    def item_id(self, item):
        return f"{item['badge_id']}&{item['user_id']}"

    def resolve_all(self):
        user_ids = list(self.repository.users.items.keys())

        badges_users = __class__._map_chunks(user_ids, 100,
            lambda chunk: self.MAPPER.load_from_users(chunk)
        )

        self.insert_list(badges_users)
