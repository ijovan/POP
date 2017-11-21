from src.main.python.data_mapping.data_mapper import DataMapper


class TagsUsersMapper(DataMapper):
    @classmethod
    def load(cls, parent_entity, parent_ids):
        tags_users = cls._http_client().get(parent_entity, parent_ids, 'tags')

        for tag_user in tags_users:
            tag_user['tag_id'] = tag_user['name']

            del tag_user['has_synonyms']
            del tag_user['is_moderator_only']
            del tag_user['is_required']
            del tag_user['name']

        return tags_users
