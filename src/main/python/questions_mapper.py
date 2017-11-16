from src.main.python.configuration import Configuration
from src.main.python.repository import Repository
from src.main.python.http_client import HttpClient
from src.main.python.mock_http_client import MockHttpClient


class QuestionsMapper:
    def get(self):
        questions = HttpClient.get('questions')['items']

        for question in questions:
            for tag in question['tags']:
                Repository().tags.insert({'name': tag})
                Repository().tags_questions.insert({
                    'tag_id': tag,
                    'question_id': question['question_id']
                })

            if question['owner']['user_type'] != 'does_not_exist':
                Repository().users.insert(
                    self.transform_user(question['owner'])
                )

            Repository().questions.insert(
                self.transform_question(question)
            )

    @staticmethod
    def http_client():
        client_class = Configuration().values()['api_client']
        globals()[client_class]

    @staticmethod
    def transform_question(question):
        question = question.copy()

        question['id'] = question['question_id']
        question['owner_id'] = question['owner']['user_id']

        del question['tags']
        del question['owner']
        del question['question_id']

        return question

    @staticmethod
    def transform_user(user):
        user = user.copy()

        user['id'] = user['user_id']
        user['type'] = user['user_type']

        del user['user_id']
        del user['user_type']

        return user
