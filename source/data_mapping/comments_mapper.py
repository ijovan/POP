from source.data_mapping.data_mapper import DataMapper
from source.resource import Resource


class CommentsMapper(DataMapper):
    REQUEST_FILTER = '!9YdnSO*ff'

    @classmethod
    def load_from_parents(cls, parent_entity, parent_ids):
        def load_chunk(chunk):
            return Resource({
                'entity': parent_entity,
                'ids': chunk,
                'submethod': 'comments',
                'query_params': {'filter': cls.REQUEST_FILTER}
            }).items()

        comments = cls._map_chunks(parent_ids, load_chunk)

        return list(map(cls.comment, comments))

    @staticmethod
    def comment(comment):
        comment['id'] = comment.pop('comment_id')

        comment['owner_id'] = \
            comment.pop('owner').pop('user_id', None)

        comment['reply_to_user_id'] = \
            comment.pop('reply_to_user', {}).pop('user_id', None)

        return comment
