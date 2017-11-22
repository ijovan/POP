from src.main.python.data_mapping.data_mapper import DataMapper
from src.main.python.resource import Resource


class AnswersMapper(DataMapper):
    REQUEST_FILTER = '!3yXvhBHjDfSUk-PqB'

    @classmethod
    def load(cls, question_ids):
        resource = Resource({
            'entity': 'questions',
            'ids': question_ids,
            'submethod': 'answers',
            'query_params': {'filter': cls.REQUEST_FILTER}
        })

        answers = resource.items()

        for answer in answers:
            answer['id'] = answer.pop('answer_id')
            answer['owner_id'] = answer.pop('owner').pop('owner_id', None)

            answer['last_editor_id'] = \
                answer.pop('last_editor', {}).pop('user_id', None)

        return answers
