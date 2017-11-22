from src.main.python.data_mapping.data_mapper import DataMapper
from src.main.python.request import Request


class AnswersMapper(DataMapper):
    REQUEST_FILTER = '!3yXvhBHjDfSUk-PqB'

    @classmethod
    def load(cls, question_ids):
        request = Request({
            'entity': 'questions',
            'ids': question_ids,
            'submethod': 'answers',
            'query_params': {'filter': cls.REQUEST_FILTER}
        })

        answers = request.items()

        for answer in answers:
            answer['id'] = answer.pop('answer_id')
            answer['owner_id'] = answer.pop('owner').pop('owner_id', None)

            answer['last_editor_id'] = \
                answer.pop('last_editor', {}).pop('user_id', None)

        return answers
