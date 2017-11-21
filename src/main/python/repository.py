from src.main.python.configuration import Configuration
from src.main.python.model.questions import Questions
from src.main.python.model.users import Users
from src.main.python.model.tags import Tags
from src.main.python.model.tags_questions import TagsQuestions
from src.main.python.model.tags_users import TagsUsers
from src.main.python.model.answers import Answers
from src.main.python.model.comments import Comments
from src.main.python.model.tag_synonyms import TagSynonyms
from src.main.python.model.badges import Badges
from src.main.python.model.badges_users import BadgesUsers
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
            instance.tags_users = TagsUsers(instance)
            instance.answers = Answers(instance)
            instance.comments = Comments(instance)
            instance.tag_synonyms = TagSynonyms(instance)
            instance.badges = Badges(instance)
            instance.badges_users = BadgesUsers(instance)

            cls.__instance = instance

        return cls.__instance

    def commit(self):
        self.questions.commit()
        self.users.commit()
        self.tags.commit()
        self.tags_questions.commit()
        self.tags_users.commit()
        self.answers.commit()
        self.comments.commit()
        self.tag_synonyms.commit()
        self.badges.commit()
        self.badges_users.commit()

    def __create_store(self):
        self.store_path = Configuration().values['store_path']

        if not os.path.isdir(self.store_path):
            os.makedirs(self.store_path)
