from src.main.python.data_mapping.data_mapper import DataMapper


class AnswersMapper(DataMapper):
    def load(self, question_ids):
        answers = self._http_client().get('questions', question_ids, 'answers')['items']

        for answer in answers:
            answer['id'] = answer['answer_id']

            if answer['owner']['user_type'] is 'does_not_exist':
                answer['owner_id'] = None
            else:
                answer['owner_id'] = answer['owner']['user_id']

            del answer['owner']
            del answer['answer_id']

            self.table.insert(answer)
