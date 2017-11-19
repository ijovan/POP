from src.main.python.data_mapper import DataMapper


class UsersMapper(DataMapper):
    def load(self, ids):
        users = self._http_client().get('users', ids)['items']

        for user in users:
            user['id'] = user['user_id']
            user['type'] = user['user_type']

            del user['user_id']
            del user['user_type']

            self.table.insert(user)
