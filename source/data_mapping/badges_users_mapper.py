from source.data_mapping.data_mapper import DataMapper
from source.resource import Resource


class BadgesUsersMapper(DataMapper):
    @classmethod
    def load_from_users(cls, user_ids):
        def load_chunk(chunk):
            return Resource({
                'entity': 'users',
                'ids': chunk,
                'submethod': 'badges'
            }).items()

        badges_users = cls._map_chunks(user_ids, load_chunk)

        return list(map(cls.badge_user, badges_users))

    @staticmethod
    def badge_user(badge_user):
        badge_user['user_id'] = badge_user.pop('user')['user_id']

        return badge_user
