import unittest
from datetime import date

from battery.spindler_battery import SpindlerBattery


class TestNubbingBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2004-01-01")
        last_service_date = date.fromisoformat("2000-01-01")
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2003-01-01")
        last_service_date = date.fromisoformat("2002-01-01")
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

