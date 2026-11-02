
from engine import Engine
from tire import Tire


class Car:
    def __init__(self, brand, hp, engine_type):
        self.brand = brand
        self.engine = Engine()
        self.engine.hp = hp
        self.engine.type = engine_type
        self.tires = [Tire() for _ in range(4)]

    def show_info(self):
        print(f"My car is a {self.brand}.")
        print(f"My car has {self.engine.hp} horsepower.")
        print(f"My car has a {self.engine.type} engine.")

        for i, tire in enumerate(self.tires, start=1):
            print(f"Tire {i} has {tire.pressure} bar.")


if __name__ == "__main__":
    my_car = Car(
        brand="Volvo V60",
        hp=392,
        engine_type="supercharged and turbocharged S4"
    )

    pressures = [2.5, 2.7, 2.8, 2.5]

    for tire, pressure in zip(my_car.tires, pressures):
        tire.pressure = pressure

    my_car.show_info()
