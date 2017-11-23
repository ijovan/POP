import os


class Credentials:
    KEY_PATH = '.key'
    ACCESS_TOKEN_PATH = '.access_token'

    @classmethod
    def key(cls):
        if Credentials._file_exists(cls.KEY_PATH):
            return open(cls.KEY_PATH).read().strip()

    @classmethod
    def access_token(cls):
        if Credentials._file_exists(cls.ACCESS_TOKEN_PATH):
            return open(cls.ACCESS_TOKEN_PATH).read().strip()

    @classmethod
    def valid(cls):
        return Credentials.key() and Credentials.access_token()

    @classmethod
    def print_warning(cls):
        print(
            "Credentials missing: please make sure that you have "
            + f"{cls.KEY_PATH} and {cls.ACCESS_TOKEN_PATH} files "
            + "in the root directory of your project. "
            + "Otherwise, you'll still be able to access the API, "
            + "but with a significantly reduced throttling limit."
        )

    @staticmethod
    def _file_exists(path):
        return os.path.isfile(path)
