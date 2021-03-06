from source.data_mapping.data_mapper import DataMapper
from source.resource import Resource
import time


class QuestionsMapper(DataMapper):
    REQUEST_FILTER = '!)5J-0UOxz87xQwv0xFNnUFSt)mFl'

    @classmethod
    def load_period(cls, params):
        resource = Resource({
            'entity': 'questions',
            'max_depth': params['max_depth'],
            'query_params': {
                'filter': cls.REQUEST_FILTER,
                'fromdate': cls.date_to_timestamp(params['from']),
                'todate': cls.date_to_timestamp(params['to'])
            }
        })

        questions = resource.items()

        return list(map(cls.question, questions))

    @staticmethod
    def question(question):
        question['id'] = question.pop('question_id')
        question['tag_ids'] = question.pop('tags')

        question['owner_id'] = \
            question.pop('owner', {}).pop('user_id', None)
        question['bounty_user_id'] = \
            question.pop('bounty_user', {}).pop('user_id', None)
        question['last_editor_id'] = \
            question.pop('last_editor', {}).pop('user_id', None)

        return question

    @staticmethod
    def date_to_timestamp(date):
        return int(time.mktime(date.timetuple()))
