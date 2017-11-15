from src.main.python.model.table import Table

class Questions(Table):
    TABLE_NAME = "questions"
    HEADER = ["id", "is_answered", "view_count", "answer_count", "score",
              "last_activity_date", "creation_date", "last_edit_date",
              "link", "title"]
