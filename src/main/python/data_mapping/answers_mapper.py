from src.main.python.data_mapping.data_mapper import DataMapper


class AnswersMapper(DataMapper):
    REQUEST_FILTER = '!3yXvhBHjDfSUk-PqB'

    @classmethod
    def load(cls, question_ids):
        answers = cls._http_client().get(
            'questions',
            question_ids,
            'answers',
            {'filter': cls.REQUEST_FILTER}
        )

        for answer in answers:
            answer['id'] = answer.pop('answer_id')
            answer['owner_id'] = answer.pop('owner').pop('owner_id', None)

            answer['last_editor_id'] = \
                answer.pop('last_editor', {}).pop('user_id', None)

        return answers
