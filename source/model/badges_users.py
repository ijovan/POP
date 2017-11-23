from source.model.table import Table
from source.data_mapping.badges_users_mapper import BadgesUsersMapper


class BadgesUsers(Table):
    TABLE_NAME = "badges_users"
    MAPPER = BadgesUsersMapper
    HEADER = ["badge_id", "user_id"]

    def item_id(self, item):
        return f"{item['badge_id']}&{item['user_id']}"

    def resolve_all(self):
        user_ids = list(self.repository.users.items.keys())

        badges_users = self.MAPPER.load_from_users(user_ids)

        self.insert_list(badges_users)
