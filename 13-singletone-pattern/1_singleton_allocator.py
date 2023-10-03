import random

class Database:
    def __init__(self):
        self.id = random.randint(1,101)
        print('Generated an id of ', self.id)
        print('Loading database')

    # check already been initialized
    _instance = None

    # Singleton by Allocator
    # check whether or not some static instance has already been created
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls)\
                .__new__(cls, *args, **kwargs)

        return cls._instance

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()

    print(d1 == d2)