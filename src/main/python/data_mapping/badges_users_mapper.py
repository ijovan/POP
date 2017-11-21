from src.main.python.data_mapping.data_mapper import DataMapper


class BadgesUsersMapper(DataMapper):
    @classmethod
    def load(cls, ids):
        badges_users = cls._http_client().get('users', ids, 'badges')

        for badge_user in badges_users:
            badge_user['user_id'] = badge_user.pop('user')['user_id']

        return badges_users
