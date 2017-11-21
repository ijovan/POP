from src.main.python.data_mapping.data_mapper import DataMapper


class UsersMapper(DataMapper):
    REQUEST_FILTER = '!-*f(6q9XCwob'

    @classmethod
    def load(cls, ids):
        users = cls._http_client().get(
            'users',
            ids,
            None,
            {'filter': cls.REQUEST_FILTER}
        )

        for user in users:
            user['id'] = user.pop('user_id')
            user['type'] = user.pop('user_type')

            badge_counts = user.pop('badge_counts')

            user['gold_badge_count'] = badge_counts['gold']
            user['silver_badge_count'] = badge_counts['silver']
            user['bronze_badge_count'] = badge_counts['bronze']

        return users
