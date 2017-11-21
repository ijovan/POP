from src.main.python.data_mapping.data_mapper import DataMapper
import time


class QuestionsMapper(DataMapper):
    REQUEST_FILTER = '!0Uv6ZT28H*3_-XcAl-jd2DZPc'

    @classmethod
    def load_period(cls, params):
        fromdate = int(time.mktime(params['from'].timetuple()))
        todate = int(time.mktime(params['to'].timetuple()))

        questions = cls._http_client().get(
            'questions',
            [],
            None,
            {'filter': cls.REQUEST_FILTER, 'fromdate': fromdate, 'todate': todate},
            {'depth': params['depth']}
        )

        for question in questions:
            question['id'] = question.pop('question_id')
            question['owner_id'] = question.pop('owner', {}).pop('user_id', None)
            question['tag_ids'] = question.pop('tags')

            question['bounty_user_id'] = \
                question.pop('bounty_user', {}).pop('user_id', None)

            question['last_editor_id'] = \
                question.pop('last_editor', {}).pop('user_id', None)


        return questions
