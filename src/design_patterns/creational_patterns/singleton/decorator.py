def singleton(cls):
    instances = {}
    def get_instances(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instances

@singleton
class MyClass:
    def __init__(self, value):
        self.value = value

if __name__ == '__main__':
    obj1 = MyClass(10)
    obj2 = MyClass(20)

    print(obj1 is obj2)
    print(obj1.value)
    print(obj2.value)