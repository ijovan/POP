from src.main.python.data_mapping.data_mapper import DataMapper


class QuestionsMapper(DataMapper):
    @classmethod
    def load_all(cls):
        questions = cls._http_client().get('questions')

        for question in questions:
            question['id'] = question['question_id']
            question['owner_id'] = question['owner']['user_id']
            question['tag_ids'] = question['tags']

            del question['tags']
            del question['owner']
            del question['question_id']

        return questions
