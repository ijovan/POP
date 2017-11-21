from src.main.python.data_mapping.data_mapper import DataMapper


class PrivilegesMapper(DataMapper):
    @classmethod
    def load_all(cls):
        privileges = cls._http_client().get('privileges')

        for privilege in privileges:
            privilege['id'] = privilege.pop('short_description')

        return privileges
