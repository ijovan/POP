from src.main.python.data_mapping.data_mapper import DataMapper
from src.main.python.request import Request


class CommentsMapper(DataMapper):
    REQUEST_FILTER = '!9YdnSO*ff'

    @classmethod
    def load(cls, parent_entity, parent_ids):
        request = Request({
            'entity': parent_entity,
            'ids': parent_ids,
            'submethod': 'comments',
            'query_params': {'filter': cls.REQUEST_FILTER}
        })

        comments = request.items()

        for comment in comments:
            comment['id'] = comment.pop('comment_id')

            comment['owner_id'] = \
                comment.pop('owner').pop('user_id', None)

            comment['reply_to_user_id'] = \
                comment.pop('reply_to_user', {}).pop('user_id', None)

        return comments
