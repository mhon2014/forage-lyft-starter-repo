from abc import ABC, abstractmethod


from battery.battery import Battery
from engine.engine import Engine


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class Car(Serviceable):
    def __init__(self, Engine: Engine, Battery: Battery):
        self.engine = Engine
        self.battery = Battery

    def needs_service(self):
        return self.engine.needs_service() \
                and self.battery.needs_service()

