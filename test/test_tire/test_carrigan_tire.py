import unittest

from tire.carrigan_tire import CarriganTire

class TestCarriganTire(unittest.TestCase):

    def test_needs_service_true(self):
        tire_sensors = [0, 0, 0, 1]
        tires = CarriganTire(tire_sensors)
        self.assertTrue(tires.needs_service())

    def test_needs_service_False(self):
        tire_sensors = [0.5, 0.5, 0.5, 0.5]
        tires = CarriganTire(tire_sensors)
        self.assertFalse(tires.needs_service())

        