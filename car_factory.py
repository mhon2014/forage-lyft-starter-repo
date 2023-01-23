from abc import ABC

from car import Car

from datetime import datetime


from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire



class CarFactory():
    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tire_sensors: list) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        calliope = Car(engine,battery)

        return calliope


    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tire_sensors: list) -> Car:
        
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        glissade = Car(engine,battery)

        return glissade


    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_on: bool, tire_sensors: list) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        palindrome = Car(engine,battery)

        return palindrome


    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tire_sensors: list) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        roschach = Car(engine,battery)

        return roschach


    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int, tire_sensors: list) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        thovex = Car(engine,battery)

        return thovex