from engine import Engine
from tire import Tire

class Car:
    def __init__(self, engine: Engine, tires: Tire):
        self.engine = engine()
        self.tires = tires()
        