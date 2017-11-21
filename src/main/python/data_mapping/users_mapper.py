from src.main.python.data_mapping.data_mapper import DataMapper


class UsersMapper(DataMapper):
    @classmethod
    def load(cls, ids):
        users = cls._http_client().get('users', ids)['items']

        for user in users:
            user['id'] = user['user_id']
            user['type'] = user['user_type']

            user['gold_badge_count'] = user['badge_counts']['gold']
            user['silver_badge_count'] = user['badge_counts']['silver']
            user['bronze_badge_count'] = user['badge_counts']['bronze']

            del user['user_id']
            del user['user_type']
            del user['badge_counts']

        return users
