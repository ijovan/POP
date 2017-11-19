from src.main.python.model.table import Table
from src.main.python.data_mapping.users_mapper import UsersMapper


class Users(Table):
    TABLE_NAME = "users"
    MAPPER_CLASS = UsersMapper
    HEADER = [
        "id", "type", "badge_counts", "account_id", "is_employee",
        "last_modified_data", "last_access_date", "age",
        "reputation_change_year", "reputation_change_quarter",
        "reputation_change_month", "reputation_change_week",
        "reputation_change_day", "reputation", "creation_date",
        "accept_rate", "location", "website_url", "link", "profile_image",
        "display_name"
    ]

    def resolve_all(self):
        ids = self.repository.questions.users()

        self.mapper.load(ids)
