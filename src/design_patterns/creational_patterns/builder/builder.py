# product
class House:
    def __init__(self):
        self.floors = None
        self.rooms = None
        self.garage = None
        self.swimming_pool = None
        self.garden = None

    def __str__(self):
        return (f"House with {self.floors} floors, {self.rooms} rooms, "
                f"{ 'a garage, ' if self.garage else 'no garage, '}"
                f"{ 'a swimming pool, ' if self.swimming_pool else 'no swimming pool, '}"
                f"{ 'a garden' if self.garden else 'no garden'}.")
    
# builder interface
from abc import ABC, abstractmethod

class HouseBuilder(ABC):
    @abstractmethod
    def set_floors(self, floors):
        pass

    @abstractmethod
    def set_rooms(self, rooms):
        pass

    @abstractmethod
    def set_garage(self, has_garage):
        pass

    @abstractmethod
    def set_swimming_pool(self, has_swimming_pool):
        pass

    @abstractmethod
    def set_garden(self, has_garden):
        pass

# concrete builder
class ConcreteHouseBuilder(HouseBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.house = House()
        return self

    def set_floors(self, floors):
        self.house.floors = floors
        return self

    def set_rooms(self, rooms):
        self.house.rooms = rooms
        return self

    def set_garage(self, has_garage):
        self.house.garage = has_garage
        return self

    def set_swimming_pool(self, has_swimming_pool):
        self.house.swimming_pool = has_swimming_pool
        return self

    def set_garden(self, has_garden):
        self.house.garden = has_garden
        return self

    def get_result(self):
        built_house = self.house
        self.reset()
        return built_house

    
# director
class HouseDirector:
    def __init__(self, builder):
        self._builder = builder

    def construct_luxury_house(self):
        return (self._builder
                .set_floors(2)
                .set_rooms(5)
                .set_garage(True)
                .set_swimming_pool(True)
                .set_garden(True)
                .get_result())

    def construct_simple_house(self):
        return (self._builder
                .set_floors(1)
                .set_rooms(2)
                .set_garage(False)
                .set_swimming_pool(False)
                .set_garden(False)
                .get_result())

    
if __name__ == '__main__':
    builder = ConcreteHouseBuilder()
    director = HouseDirector(builder)

    luxury_house = director.construct_luxury_house()
    simple_house = director.construct_simple_house()

    print(luxury_house)
    print(simple_house)