class Singleton:
    __instance = None

    def __new__(cls):
        if Singleton.__instance is None:
            print("INSTANTIATING")
            Singleton.__instance = object.__new__(cls)
        return Singleton.__instance

print(Singleton())
print(Singleton())
