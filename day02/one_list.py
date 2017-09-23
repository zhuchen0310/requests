class CarFactory(object):
    __first_new = True
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__first_new:
            cls.__instance = object.__new__(cls)
            cls.__first_new = False
            return cls.__instance
        else:
            return cls.__instance