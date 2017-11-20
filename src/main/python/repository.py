from src.main.python.configuration import Configuration
from src.main.python.model.questions import Questions
from src.main.python.model.users import Users
from src.main.python.model.tags import Tags
from src.main.python.model.tags_questions import TagsQuestions
from src.main.python.model.answers import Answers
import os


class Repository:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            instance = object.__new__(cls)

            instance.__create_store()
            instance.questions = Questions(instance)
            instance.users = Users(instance)
            instance.tags = Tags(instance)
            instance.tags_questions = TagsQuestions(instance)
            instance.answers = Answers(instance)

            cls.__instance = instance

        return cls.__instance

    def commit(self):
        self.questions.commit()
        self.users.commit()
        self.tags.commit()
        self.tags_questions.commit()
        self.answers.commit()

    def __create_store(self):
        self.store_path = Configuration().values['store_path']

        if not os.path.isdir(self.store_path):
            os.makedirs(self.store_path)
