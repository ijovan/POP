from src.main.python.data_mapping.data_mapper import DataMapper
from src.main.python.resource import Resource


class BadgesUsersMapper(DataMapper):
    @classmethod
    def load_from_users(cls, user_ids):
        resource = Resource({
            'entity': 'users',
            'ids': user_ids,
            'submethod': 'badges'
        })

        badges_users = resource.items()

        for badge_user in badges_users:
            badge_user['user_id'] = badge_user.pop('user')['user_id']

        return badges_users
