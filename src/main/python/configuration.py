import json


class Configuration:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            instance = object.__new__(cls)
            instance.environment = None
            instance.values = {}
            cls.__instance = instance

        return cls.__instance

    @classmethod
    def set_test_environment(cls):
        cls().__set_environment('test')

    @classmethod
    def set_prod_environment(cls):
        cls().__set_environment('prod')

    def __set_environment(self, environment_name):
        self.environment = environment_name

        self.__load_config()

    def __load_config(self):
        file_path = f"config/{self.environment}.json"

        self.values = json.load(open(file_path))
