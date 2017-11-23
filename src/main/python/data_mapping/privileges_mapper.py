from src.main.python.data_mapping.data_mapper import DataMapper
from src.main.python.resource import Resource


class PrivilegesMapper(DataMapper):
    @classmethod
    def load_all(cls):
        privileges = Resource({'entity': 'privileges'}).items()

        return list(map(cls.privilege, privileges))

    @staticmethod
    def privilege(privilege):
        privilege['id'] = privilege.pop('short_description')

        return privilege
