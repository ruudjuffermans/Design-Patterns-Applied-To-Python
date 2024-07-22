class Dog:
    def speak(self):
        return "Woof!"
              
class Cat:
    def speak(self):
        return "Meow!"
    

class AnimalFactory:

    _creators = {
        'dog': Dog,
        'cat': Cat
    }

    @classmethod
    def create_animal(cls, animal_type):
        if animal_type in cls._creators:
            return  cls._creators[animal_type]()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")
    
if __name__=="__main__":
    dog = AnimalFactory.create_animal("dog")
    cat = AnimalFactory.create_animal("cat")

    print(dog.speak())
    print(cat.speak())