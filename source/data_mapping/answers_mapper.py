from source.data_mapping.data_mapper import DataMapper
from source.resource import Resource


class AnswersMapper(DataMapper):
    REQUEST_FILTER = '!3yXvhBHjDfSUk-PqB'

    @classmethod
    def load_from_questions(cls, question_ids):
        def load_chunk(chunk):
            return Resource({
                'entity': 'questions',
                'ids': chunk,
                'submethod': 'answers',
                'query_params': {'filter': cls.REQUEST_FILTER}
            }).items()

        answers = cls._map_chunks(question_ids, load_chunk)

        return list(map(cls.answer, answers))

    @staticmethod
    def answer(answer):
        answer['id'] = answer.pop('answer_id')
        answer['owner_id'] = answer.pop('owner').pop('user_id', None)

        answer['last_editor_id'] = \
            answer.pop('last_editor', {}).pop('user_id', None)

        return answer
