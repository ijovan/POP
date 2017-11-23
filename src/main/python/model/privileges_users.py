from src.main.python.model.table import Table


class PrivilegesUsers(Table):
    TABLE_NAME = "privileges_users"
    HEADER = ["privilege_id", "user_id"]

    def item_id(self, item):
        return f"{item['privilege_id']}&{item['user_id']}"

    def resolve_all(self):
        privileges = list(self.repository.privileges.items.values())
        users = list(self.repository.users.items.values())

        privileges_users = []

        for user in users:
            for privilege in privileges:
                if privilege['reputation'] <= user['reputation']:
                    privileges_users.append({
                        'privilege_id': privilege['id'],
                        'user_id': user['id']
                    })

        self.insert_list(privileges_users)
