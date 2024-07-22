class Dog:
    def speak(self):
        return "Woof!"
              
class Cat:
    def speak(self):
        return "Meow!"
    

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return  Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")
    
if __name__=="__main__":
    factory = AnimalFactory()
    dog = factory.create_animal("dog")
    cat = factory.create_animal("cat")

    print(dog.speak())
    print(cat.speak())