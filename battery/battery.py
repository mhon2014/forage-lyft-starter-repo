from abc import ABC, abstractmethod

from datetime import datetime

'''
Interface for battery class
'''


class Battery(ABC):

    @abstractmethod
    def needs_service(self) -> bool:
        pass

class SpindlerBattery(Battery):
    def __init__(self, last_service_date: datetime, current_date: datetime):
        self.last_service_date: last_service_date      
        self.current_date: current_date

    def needs_service(self) -> bool:
        year_threshold = self.last_service_date.replace(year=self.last_service_date.year + 2)
        return self.current_date.year >= year_threshold


class NubbinBattery(Battery):
    def __init__(self, last_service_date: datetime, current_date: datetime):
        self.last_service_date: last_service_date      
        self.current_date: current_date

    def needs_service(self) -> bool:
        year_threshold = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return self.current_date.year >= year_threshold
