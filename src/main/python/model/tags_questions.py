from src.main.python.model.table import Table


class TagsQuestions(Table):
    TABLE_NAME = "tags_questions"
    HEADER = ["tag_id", "question_id"]

    def _id(self, item):
        return f"{item['tag_id']}&{item['question_id']}"

    def resolve_all(self):
        tags_questions = self.repository.questions.tags()

        self.insert_list(tags_questions)
