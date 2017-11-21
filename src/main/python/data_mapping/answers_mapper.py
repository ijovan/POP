from src.main.python.data_mapping.data_mapper import DataMapper


class AnswersMapper(DataMapper):
    @classmethod
    def load(cls, question_ids):
        answers = cls._http_client().get('questions', question_ids, 'answers')

        for answer in answers:
            answer['id'] = answer.pop('answer_id')
            answer['owner_id'] = answer.pop('owner').pop('owner_id', None)

        return answers
