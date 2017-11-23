from source.data_mapping.data_mapper import DataMapper
from source.resource import Resource


class UsersMapper(DataMapper):
    REQUEST_FILTER = '!-*f(6q9XCwob'

    @classmethod
    def load(cls, ids):
        def load_chunk(chunk):
            return Resource({
                'entity': 'users',
                'ids': chunk,
                'query_params': {'filter': cls.REQUEST_FILTER}
            }).items()

        users = cls._map_chunks(ids, load_chunk)

        return list(map(cls.user, users))

    @staticmethod
    def user(user):
        user['id'] = user.pop('user_id')
        user['type'] = user.pop('user_type')

        badge_counts = user.pop('badge_counts')

        user['gold_badge_count'] = badge_counts['gold']
        user['silver_badge_count'] = badge_counts['silver']
        user['bronze_badge_count'] = badge_counts['bronze']

        return user
