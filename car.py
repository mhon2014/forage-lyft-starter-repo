from abc import ABC, abstractmethod


from battery.battery import Battery
from engine.engine import Engine
from tire.tire import Tire


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class Car(Serviceable):
    def __init__(self, Engine: Engine, Battery: Battery, Tire: Tire):
        self.engine = Engine
        self.battery = Battery
        self.tire = Tire

    def needs_service(self):
        return self.engine.needs_service() \
                or self.battery.needs_service() \
                or self.tire.needs_service()

