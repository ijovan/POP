from source.model.table import Table
from source.data_mapping.privileges_mapper import PrivilegesMapper


class Privileges(Table):
    TABLE_NAME = "privileges"
    MAPPER = PrivilegesMapper
    HEADER = ["id", "reputation", "description"]

    def resolve_all(self):
        privileges = self.MAPPER.load_all()

        self.insert_list(privileges)
