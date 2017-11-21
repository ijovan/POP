from src.main.python.data_mapping.data_mapper import DataMapper


class CommentsMapper(DataMapper):
    @classmethod
    def load(cls, parent_entity, parent_ids):
        comments = cls._http_client().get(parent_entity, parent_ids, 'comments')

        for comment in comments:
            comment['id'] = comment['comment_id']

            comment['owner_id'] = \
                cls.transform_user(comment['owner'])

            if 'reply_to_user' in list(comment.keys()):
                comment['reply_to_user_id'] = \
                    cls.transform_user(comment['reply_to_user'])
                del comment['reply_to_user']

            del comment['comment_id']
            del comment['owner']

        return comments

    def transform_user(user):
        if user['user_type'] is 'does_not_exist':
            return None
        else:
            return user['user_id']
