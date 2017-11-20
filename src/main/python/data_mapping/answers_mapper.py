from src.main.python.data_mapping.data_mapper import DataMapper


class AnswersMapper(DataMapper):
    def load(self, question_ids):
        answers = self._http_client().get('questions', question_ids, 'answers')['items']

        for answer in answers:
            answer['id'] = answer['answer_id']
            answer['owner_id'] = answer['owner']['user_id']

            del answer['answer_id']

            self.table.insert(answer)
