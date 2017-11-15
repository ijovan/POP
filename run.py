from src.main.python.data_source import DataSource
from src.main.python.model.questions import Questions

questions = DataSource.get_questions()
Questions.insert(questions)
