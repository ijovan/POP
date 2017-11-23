from src.main.python.data_mapping.data_mapper import DataMapper
from src.main.python.resource import Resource


class TagsUsersMapper(DataMapper):
    CHUNK_SIZE = 20

    @classmethod
    def load_from_users(cls, user_ids):
        def load_chunk(chunk):
            return Resource({
                'entity': 'users',
                'ids': chunk,
                'submethod': 'tags'
            }).items()

        tags_users = cls._map_chunks(user_ids, load_chunk)

        return list(map(cls.tag_user, tags_users))

    @staticmethod
    def tag_user(tag_user):
        tag_user['tag_id'] = tag_user.pop('name')

        del tag_user['has_synonyms']
        del tag_user['is_moderator_only']
        del tag_user['is_required']

        return tag_user
