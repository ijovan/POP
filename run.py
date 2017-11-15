from src.main.python.data_source import DataSource
from src.main.python.model.questions import Questions
from src.main.python.model.users import Users
from src.main.python.model.tags import Tags
from src.main.python.model.tags_questions import TagsQuestions

def pull_questions():
    result_set = DataSource.query_questions()

    Questions.insert(result_set['questions'])
    Users.insert(result_set['users'])
    Tags.insert(result_set['tags'])
    TagsQuestions.insert(result_set['tags_questions'])

pull_questions()
