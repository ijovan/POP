from src.main.python.model.table import Table


class Users(Table):
    TABLE_NAME = "users"
    HEADER = ["id", "type", "reputation", "profile_image", "display_name",
              "link"]
