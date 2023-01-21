from abc import ABC

from car.car import Car

from datetime import datetime

from battery.battery import *

from engine.engine import *


class CarFactory(ABC):
    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine()
        battery = SpindlerBattery()
        calliope = Car(engine,battery)

        return calliope


    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        pass


    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_on: bool) -> Car:
        pass


    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        pass


    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        pass

    