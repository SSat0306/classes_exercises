"""
1. Create a class according to the following requirements:
It's name is Vehicle and it has the following attributes/methods:
Attributes/properties:
  name: str
  max_speed: int
  capacity: int
Methods:
    vroom() -> None
        Prints "Vroom" max_speed times
2. Create a child/subclass of Vehicle called Bus with the following methods:
Methods:
    fare(age: float) -> None
        Prints "The fare of the bus ride is {}."
            Price depends on age:
                0-17 years - Free
                18-60 years - $5
                61+ years - Free
"""


class Vehicle():
    def __init__(self):
        self.name = ""
        self.max_speed = 0
        self.capacity = 0

    def vroom(self):
        print("Vroom" * self.max_speed)

class Bus(Vehicle):
    """Bus is a Vehicle that can drive humans around in it"""
    def fare(self, age: int) -> None:
        """Tells how huch fare is for a particular age"""
        if 19 <= age <= 61:
            print("You fare of this bus is $5")
        else:
            print("You ride free")
a_vehicle = Vehicle()
a_vehicle.name = "La Ferrari"
a_vehicle.max_speed = 372
a_vehicle.capacity = 2
a_bus = Bus()
a_bus.name = "Translink Bus - 487"
a_bus.max_speed = 148
a_bus.fare(10)
a_bus.fare(12)


