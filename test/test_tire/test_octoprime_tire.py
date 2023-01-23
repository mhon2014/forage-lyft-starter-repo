import unittest

from tire.octoprime_tire import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):

    def test_needs_service_true(self):
        tire_sensors = [0, 1, 1, 1]
        tires = OctoprimeTire(tire_sensors)
        self.assertTrue(tires.needs_service())

    def test_needs_service_False(self):
        tire_sensors = [0.5, 0.5, 0.5, 0.5]
        tires = OctoprimeTire(tire_sensors)
        self.assertFalse(tires.needs_service())

        