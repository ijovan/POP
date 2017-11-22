from src.main.python.data_mapping.data_mapper import DataMapper
from src.main.python.resource import Resource


class PrivilegesMapper(DataMapper):
    @classmethod
    def load_all(cls):
        resource = Resource({'entity': 'privileges'})

        privileges = resource.items()

        for privilege in privileges:
            privilege['id'] = privilege.pop('short_description')

        return privileges
