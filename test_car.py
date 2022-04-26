import unittest
from car import Car as C


class TestOnTheRoad(unittest.TestCase):
    def setUp(self):
        self.car_1 = C("abc1234", "Tuesday", "07:25")
        self.car_2 = C("abc1234", "Tuesday", "13:25")
        self.car_3 = C("abc1234", "Tuesday", "17:25")

    def test_restriction(self):
        self.assertEqual(self.car_1.has_mobility_restriction(), True)
        self.assertEqual(self.car_2.has_mobility_restriction(), False)
        self.assertEqual(self.car_3.has_mobility_restriction(), True)


if __name__ == "__main__":
    unittest.main()
