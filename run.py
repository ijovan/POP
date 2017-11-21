from src.main.python.repository import Repository
from src.main.python.configuration import Configuration


def pull_questions():
    repository = Repository()

    repository.questions.load_all()
    repository.resolve()
    repository.commit()

Configuration().set_prod_environment()
pull_questions()
