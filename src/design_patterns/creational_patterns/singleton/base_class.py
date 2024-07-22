class SingletonBase:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonBase, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
class MyClass(SingletonBase):
    def __init__(self, value):
        if not hasattr(self, 'initialized'):
            self.value = value
            self.initialized = True

if __name__ == '__main__':
    obj1 = MyClass(10)
    obj2 = MyClass(20)

    print(obj1 is obj2)
    print(obj1.value)
    print(obj2.value)