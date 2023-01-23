from tire.tire import Tire

class CarriganTire(Tire):
    
    def __init__(self, tire_sensors: list):
        self.tire_sensors = tire_sensors
        

    def needs_service(self) -> bool:
        for value in self.tire_sensors:
            if float(value) >= 0.9:
                return True
        
        return False