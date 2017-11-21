from src.main.python.data_mapping.data_mapper import DataMapper


class CommentsMapper(DataMapper):
    REQUEST_FILTER = '!9YdnSO*ff'

    @classmethod
    def load(cls, parent_entity, parent_ids):
        comments = cls._http_client().get(
            parent_entity,
            parent_ids,
            'comments',
            {'filter': cls.REQUEST_FILTER}
        )

        for comment in comments:
            comment['id'] = comment.pop('comment_id')

            comment['owner_id'] = \
                comment.pop('owner').pop('user_id', None)

            comment['reply_to_user_id'] = \
                comment.pop('reply_to_user', {}).pop('user_id', None)

        return comments
