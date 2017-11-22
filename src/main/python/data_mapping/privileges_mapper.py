from src.main.python.data_mapping.data_mapper import DataMapper
from src.main.python.request import Request


class PrivilegesMapper(DataMapper):
    @classmethod
    def load_all(cls):
        request = Request({'entity': 'privileges'})

        privileges = request.items()

        for privilege in privileges:
            privilege['id'] = privilege.pop('short_description')

        return privileges
