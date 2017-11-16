from src.main.python.questions_mapper import QuestionsMapper
from src.main.python.repository import Repository
from src.main.python.configuration import Configuration


def pull_questions():
    result_set = QuestionsMapper().get()

    Repository().commit()

Configuration().set_test_environment()
pull_questions()
