class Dog:
    def speak(self):
        return "Woof!"
              
class Cat:
    def speak(self):
        return "Meow!"
    
def animal_factory(animal_type):
    if animal_type == "dog":
        return  Dog()
    elif animal_type == "cat":
        return Cat()
    else:
        raise ValueError(f"Unknown animal type: {animal_type}")
    
if __name__ == "__main__":
    dog = animal_factory("dog")
    cat = animal_factory("cat")

    print(dog.speak())
    print(cat.speak())