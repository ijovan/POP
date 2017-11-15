from src.main.python.http_client import HttpClient

class DataSource:
    @classmethod
    def query_questions(cls):
        questions = HttpClient.get('questions')['items']

        tags = {}
        users = []

        for question in questions:
            for tag in question['tags']:
                if not tag in tags.keys():
                    tags[tag] = {'id': len(tags), 'name': tag}

            user = cls.transform_user(question['owner'])
            question['owner_id'] = user['id']
            users = users + [user]

            question = cls.transform_question(question)

        return {
            'questions': questions,
            'tags': list(tags.values()),
            'users': users
        }

    @staticmethod
    def transform_question(question):
        question['id'] = question['question_id']

        del question['tags']
        del question['owner']
        del question['question_id']

        return question

    @staticmethod
    def transform_user(user):
        user['id'] = user['user_id']
        user['type'] = user['user_type']

        del user['user_id']
        del user['user_type']

        return user
