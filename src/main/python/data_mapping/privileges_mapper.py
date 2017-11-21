from src.main.python.data_mapping.data_mapper import DataMapper


class PrivilegesMapper(DataMapper):
    @classmethod
    def load_all(cls):
        privileges = cls._http_client().get('privileges')['items']

        for privilege in privileges:
            privilege['id'] = privilege['short_description']

            del privilege['short_description']

        return privileges
