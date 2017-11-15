from src.main.python.http_client import HttpClient

class DataSource:
    def get_questions():
        content = HttpClient.get("questions")

        items = content['items']

        for item in items:
            item['id'] = item['question_id']

            del item['tags']
            del item['owner']
            del item['question_id']

        return items
