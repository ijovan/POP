from src.main.python.model.table import Table
from src.main.python.data_mapping.users_mapper import UsersMapper


class Users(Table):
    TABLE_NAME = "users"
    MAPPER = UsersMapper
    HEADER = [
        "id", "type", "account_id", "is_employee", "last_modified_data",
        "last_access_date", "age", "reputation_change_year",
        "reputation_change_quarter", "reputation_change_month",
        "reputation_change_week", "reputation_change_day", "reputation",
        "creation_date", "accept_rate", "location", "website_url", "link",
        "profile_image", "display_name"
    ]

    def resolve_all(self):
        ids_from_questions = self.repository.questions.users()
        ids_from_answers = self.repository.answers.users()
        ids_from_comments = self.repository.comments.users()

        ids = list(
            set(ids_from_questions) |
            set(ids_from_answers) |
            set(ids_from_comments)
        )

        users = self.MAPPER.load(ids)

        self.insert_list(users)
