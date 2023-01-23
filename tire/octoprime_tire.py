from tire.tire import Tire

class OctoprimeTire(Tire):

    def __init__(self, tire_sensors: list):
        self.tire_sensors = tire_sensors
        

    def needs_service(self) -> bool:
        sum = 0
        for value in self.tire_sensors:
            sum += value
        
        if sum >= 3:
            return True
        
        return False