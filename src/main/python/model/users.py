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
        "profile_image", "display_name", "gold_badge_count",
        "silver_badge_count", "bronze_badge_count", "answer_count",
        "down_vote_count", "question_count", "up_vote_count", "view_count"
    ]

    def resolve_all(self):
        ids = list(filter(None,
            set(self.repository.questions.users()) |
            set(self.repository.answers.users()) |
            set(self.repository.comments.users())
        ))

        users = self.MAPPER.load(ids)

        self.insert_list(users)
