from src.main.python.data_mapper import DataMapper


class QuestionsMapper(DataMapper):
    def load_all(self):
        questions = self._http_client().get('questions')['items']

        for question in questions:
            question['id'] = question['question_id']
            question['owner_id'] = question['owner']['user_id']
            question['tag_ids'] = question['tags']

            del question['tags']
            del question['owner']
            del question['question_id']

            self.table.insert(question)
