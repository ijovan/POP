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
from src.main.python.model.privileges import Privileges
from src.main.python.model.privileges_users import PrivilegesUsers
import os


class Repository:
    STORE_PATH = "output"
    KEY_CACHE_PATH = f"{STORE_PATH}/.key_cache"

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            instance = object.__new__(cls)

            instance.__create_store()
            instance.questions = Questions(instance)
            instance.answers = Answers(instance)
            instance.comments = Comments(instance)
            instance.users = Users(instance)
            instance.tags_questions = TagsQuestions(instance)
            instance.tags_users = TagsUsers(instance)
            instance.tags = Tags(instance)
            instance.tag_synonyms = TagSynonyms(instance)
            instance.badges = Badges(instance)
            instance.badges_users = BadgesUsers(instance)
            instance.privileges = Privileges(instance)
            instance.privileges_users = PrivilegesUsers(instance)

            cls.__instance = instance

        return cls.__instance

    def resolve(self):
        self.answers.resolve_all()
        self.comments.resolve_all()
        self.users.resolve_all()
        self.tags_questions.resolve_all()
        # self.tags_users.resolve_all()
        self.tags.resolve_all()
        self.tag_synonyms.resolve_all()
        # self.badges_users.resolve_all()
        # self.badges.resolve_all()
        # self.privileges.resolve_all()
        # self.privileges_users.resolve_all()

    def commit(self):
        self.questions.commit()
        self.answers.commit()
        self.comments.commit()
        self.users.commit()
        self.tags_questions.commit()
        self.tags_users.commit()
        self.tags.commit()
        self.tag_synonyms.commit()
        self.badges_users.commit()
        self.badges.commit()
        self.privileges.commit()
        self.privileges_users.commit()

        print("COMMIT SUCCESSFUL")

    def __create_store(self):
        if not os.path.isdir(self.STORE_PATH):
            os.makedirs(self.STORE_PATH)

        if not os.path.isdir(self.KEY_CACHE_PATH):
            os.makedirs(self.KEY_CACHE_PATH)
