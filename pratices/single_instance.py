class Singleton(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance


if __name__ == '__main__':
    a = Singleton()
    b = Singleton()
    print(id(a) == id(b))
    print(a is b)
