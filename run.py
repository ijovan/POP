from src.main.python.repository import Repository
from src.main.python.configuration import Configuration


def pull_questions():
    repository = Repository()

    repository.questions.load_all()
    repository.tags.resolve_all()
    repository.tags_questions.resolve_all()
    repository.answers.resolve_all()
    repository.comments.resolve_all()
    repository.users.resolve_all()

    repository.commit()

Configuration().set_prod_environment()
pull_questions()
