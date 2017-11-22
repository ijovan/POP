from src.main.python.data_mapping.data_mapper import DataMapper
from src.main.python.resource import Resource


class TagsUsersMapper(DataMapper):
    @classmethod
    def load_from_users(cls, user_ids):
        resource = Resource({
            'entity': 'users',
            'ids': user_ids,
            'submethod': 'tags'
        })

        tags_users = resource.items()

        for tag_user in tags_users:
            tag_user['tag_id'] = tag_user.pop('name')

            del tag_user['has_synonyms']
            del tag_user['is_moderator_only']
            del tag_user['is_required']

        return tags_users
