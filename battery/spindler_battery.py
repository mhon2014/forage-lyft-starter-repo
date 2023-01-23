
from battery.battery import Battery
from datetime import datetime

class SpindlerBattery(Battery):
    def __init__(self, last_service_date: datetime, current_date: datetime):
        self.last_service_date = last_service_date      
        self.current_date = current_date

    def needs_service(self) -> bool:
        year_threshold = self.last_service_date.replace(year=self.last_service_date.year + 3)
        return self.current_date >= year_threshold
